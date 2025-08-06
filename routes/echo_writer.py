# routes/echo_writer.py

import os
from flask import Blueprint, render_template, request, session, redirect, url_for
from werkzeug.utils import secure_filename
from languages import get_lang_config, get_translations
from services.whispercpp import transcribe
from pydub import AudioSegment

bp = Blueprint("echo_writer", __name__, template_folder="../templates")

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@bp.route("/", methods=["GET", "POST"])
def echo_writer():
    lang_code = request.args.get('lang', 'en')
    lang_config = get_lang_config(lang_code)
    translations = get_translations(lang_code)
    
    # Get the result from the session if it exists
    transcription_result = session.pop('transcription_result', None)

    if request.method == "POST":
        audio_file = request.files.get('audio')
        temp_webm_path = None
        temp_wav_path = None
        
        if audio_file:
            try:
                filename_webm = secure_filename("user_recording.webm")
                temp_webm_path = os.path.join(UPLOAD_FOLDER, filename_webm)
                audio_file.save(temp_webm_path)
                
                filename_wav = "user_recording.wav"
                temp_wav_path = os.path.join(UPLOAD_FOLDER, filename_wav)
                sound = AudioSegment.from_file(temp_webm_path, format="webm")
                sound.export(temp_wav_path, format="wav")

                transcribed_text = transcribe(temp_wav_path)
                
                if transcribed_text:
                    session['transcription_result'] = {"text": transcribed_text}
                else:
                    session['transcription_result'] = {"error": "Could not understand the audio. Please try again."}
            
            except Exception as e:
                session['transcription_result'] = {"error": f"An unexpected error occurred: {e}"}
            finally:
                if temp_webm_path and os.path.exists(temp_webm_path):
                    os.remove(temp_webm_path)
                if temp_wav_path and os.path.exists(temp_wav_path):
                    os.remove(temp_wav_path)
        else:
            session['transcription_result'] = {"error": "No audio file was received."}

        # Redirect back to this same page (will be a GET request)
        return redirect(url_for('echo_writer.echo_writer', lang=lang_code))

    # This 'return' now handles both the initial load and the load after a redirect
    return render_template(
        "echo_writer.html",
        lang_config=lang_config,
        lang_code=lang_code,
        t=translations,
        result=transcription_result
    )
