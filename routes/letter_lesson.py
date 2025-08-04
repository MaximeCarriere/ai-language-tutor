import os
import json
import subprocess
from flask import Blueprint, render_template, request, current_app
from services.ollama import call_gemma_cli
from services.whispercpp import transcribe
from services.feedback import normalize_feedback
from persistence.lessons import load_letter_lesson
from persistence.progress import log_vocab_attempt
from prompts import build_phoneme_prompt, build_word_practice_prompt
from werkzeug.utils import secure_filename

bp = Blueprint("letter_lesson", __name__, template_folder="../templates")

# relative to project root; ensure exists
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def convert_to_wav(src_path: str) -> str:
    """
    Convert audio to 16kHz mono WAV via ffmpeg if needed.
    Returns path to wav (might be same base with .wav).
    """
    base, _ = os.path.splitext(src_path)
    wav_path = f"{base}.wav"
    if os.path.exists(wav_path):
        return wav_path
    try:
        subprocess.run(
            ["ffmpeg", "-y", "-i", src_path, "-ar", "16000", "-ac", "1", wav_path],
            capture_output=True,
            text=True,
            check=True,
            timeout=10,
        )
        return wav_path
    except subprocess.CalledProcessError as e:
        current_app.logger.warning("ffmpeg conversion failed: %s", e.stderr or e)
    except Exception as e:
        current_app.logger.warning("ffmpeg conversion error: %s", e)
    return ""

@bp.route("", methods=["GET", "POST"])
def letter_lesson():
    letter = request.args.get("letter", "A").upper()
    current_app.logger.debug("Entered letter_lesson for letter=%s method=%s", letter, request.method)
    lesson = load_letter_lesson(letter)
    intro = lesson.get("intro", "")
    fonts = lesson.get("fonts", [])
    phonemes = lesson.get("phonemes", [])
    words = lesson.get("words", [])
    phoneme_result = None
    word_result = None
    message = None

    if request.method == "POST":
        sub = request.form.get("sub")
        current_app.logger.debug("Processing subexercise: %s", sub)

        if sub == "phoneme":
            symbol = request.form.get("symbol", "")
            attempt = request.form.get("phoneme_attempt", "").strip()

            audio_file = request.files.get("phoneme_audio")
            if audio_file and audio_file.filename:
                filename = secure_filename(audio_file.filename)
                audio_path = os.path.join(UPLOAD_FOLDER, filename)
                audio_file.save(audio_path)
                current_app.logger.info("Received audio for phoneme '%s' at %s", symbol, audio_path)

                wav_path = convert_to_wav(audio_path)
                if wav_path:
                    transcribed = transcribe(wav_path)
                    if transcribed:
                        attempt = transcribed
                        current_app.logger.debug("Transcribed phoneme attempt: %s", attempt)
                    else:
                        message = "Audio transcription failed; using typed approximation."
                        current_app.logger.warning("whisper.cpp returned empty transcription for %s", wav_path)
                else:
                    message = "Audio conversion failed; using typed approximation."
                    current_app.logger.warning("Failed to get wav for %s", audio_path)
            else:
                current_app.logger.debug("No audio provided for phoneme '%s'; using typed attempt '%s'", symbol, attempt)

            prompt = build_phoneme_prompt(symbol, attempt)
            current_app.logger.debug("Sending prompt to Gemma for phoneme '%s': %.100s", symbol, prompt)
            raw = call_gemma_cli(prompt)
            current_app.logger.debug("Raw Gemma output (phoneme): %.300s", raw)
            feedback_text = normalize_feedback(raw)
            phoneme_result = {
                "target_phoneme": symbol,
                "feedback": feedback_text,
            }
            log_vocab_attempt(
                f"LetterLesson phoneme {symbol}",
                attempt,
                {"level": "A", "sublevel": f"phoneme:{symbol}", "result": phoneme_result},
            )

        elif sub == "word":
            word = request.form.get("word", "")
            attempt = request.form.get("word_attempt", "").strip()

            audio_file = request.files.get("word_audio")
            if audio_file and audio_file.filename:
                filename = secure_filename(audio_file.filename)
                audio_path = os.path.join(UPLOAD_FOLDER, filename)
                audio_file.save(audio_path)
                current_app.logger.info("Received audio for word '%s' at %s", word, audio_path)

                wav_path = convert_to_wav(audio_path)
                if wav_path:
                    transcribed = transcribe(wav_path)
                    if transcribed:
                        attempt = transcribed
                        current_app.logger.debug("Transcribed word attempt: %s", attempt)
                    else:
                        message = "Audio transcription failed; using typed word."
                        current_app.logger.warning("whisper.cpp returned empty transcription for %s", wav_path)
                else:
                    message = "Audio conversion failed; using typed word."
                    current_app.logger.warning("Failed to get wav for %s", audio_path)
            else:
                current_app.logger.debug("No audio provided for word '%s'; using typed attempt '%s'", word, attempt)

            prompt = build_word_practice_prompt(word, attempt)
            current_app.logger.debug("Sending prompt to Gemma for word '%s': %.100s", word, prompt)
            raw = call_gemma_cli(prompt)
            current_app.logger.debug("Raw Gemma output (word): %.300s", raw)
            try:
                word_result = json.loads(raw.strip().splitlines()[-1])
            except Exception:
                word_result = {"error": raw}
            log_vocab_attempt(
                f"LetterLesson word {word}",
                attempt,
                {"level": "A", "sublevel": f"word:{word}", "result": word_result},
            )

    return render_template(
        "letter_lesson.html",
        letter=letter,
        lesson=lesson,
        intro=intro,
        fonts=fonts,
        phonemes=phonemes,
        words=words,
        phoneme_result=phoneme_result,
        word_result=word_result,
        message=message,
    )
