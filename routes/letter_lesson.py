# routes/letter_lesson.py

import json
from flask import Blueprint, render_template, request
from languages import get_lang_config, get_translations, get_letter_lesson
from services.ollama import call_gemma_cli

bp = Blueprint("letter_lesson", __name__, template_folder="../templates")

@bp.route("/", methods=["GET", "POST"])
def show_lesson():
    lang_code = request.args.get('lang', 'en')
    letter = request.args.get('letter', 'A' if lang_code == 'en' else 'أ')
    
    lang_config = get_lang_config(lang_code)
    translations = get_translations(lang_code)
    lesson_data = get_letter_lesson(lang_code, letter)
    
    phoneme_result = None
    word_result = None

    # --- ADDED: Logic to get context letters ---
    alphabet = lang_config.get('alphabet_upper', lang_config['alphabet'])
    context_letters = ""
    try:
        # Find the index of the current letter in the alphabet
        idx = alphabet.index(letter.upper())
        # Define how many letters to show on each side
        context_window = 2
        start = max(0, idx - context_window)
        end = min(len(alphabet), idx + context_window + 1)
        context_letters = alphabet[start:end]
    except (ValueError, KeyError):
        # Fallback if letter not in alphabet or alphabet_upper not defined
        context_letters = letter.upper()
    # ------------------------------------------

    if request.method == "POST":
        if request.form.get('sub') == 'phoneme':
             phoneme_result = {
                 "target_phoneme": request.form.get('symbol'),
                 "correct": True,
                 "feedback": "You pronounced the sound perfectly!"
             }
        elif request.form.get('sub') == 'word':
            word_result = {
                "word": request.form.get('word'),
                "correct": False,
                "feedback": "That was a good attempt. Let's try that word again."
            }

    return render_template(
        "letter_lesson.html",
        letter=letter,
        lang_config=lang_config,
        t=translations,
        lesson=lesson_data,
        phoneme_result=phoneme_result,
        word_result=word_result,
        context_letters=context_letters  # Pass the new variable to the template
    )
