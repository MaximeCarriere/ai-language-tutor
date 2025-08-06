# routes/letter.py

from flask import Blueprint, render_template, request, jsonify
from languages import get_lang_config, get_translations

# The blueprint now points to the main Letter Hub
bp = Blueprint("letter", __name__, template_folder="../templates")

@bp.route("/")
def letter_hub():
    """Renders the main letter hub page with the full alphabet."""
    lang_code = request.args.get('lang', 'en')
    lang_config = get_lang_config(lang_code)
    translations = get_translations(lang_code)

    return render_template(
        "letter.html",
        lang_config=lang_config,
        lang_code=lang_code,
        t=translations
    )

@bp.route("/letter_sound")
def letter_sound():
    """Provides the text-to-speech string for a given letter and language."""
    lang_code = request.args.get('lang', 'en')
    letter = request.args.get('letter', 'A')
    
    speak_text = f"This is the letter {letter}."
    if lang_code == 'ar':
        speak_text = f"هذا حرف {letter}"
    elif lang_code == 'prs':
        speak_text = f"این حرف {letter} است"

    return jsonify({"speak_text": speak_text})
