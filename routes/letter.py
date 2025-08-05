import json
from flask import Blueprint, render_template, request, jsonify
from services.ollama import call_gemma_cli
from persistence.progress import log_vocab_attempt
from prompts import build_letter_prompt
# Import both helpers from the 'languages' module
from languages import get_lang_config, get_translations

bp = Blueprint("letter", __name__, template_folder="../templates")

@bp.route("/", methods=["GET", "POST"])
def letter_practice():
    # Get language from URL query, default to English
    lang_code = request.args.get('lang', 'en')
    
    # Get the language-specific configuration (alphabet, font, etc.)
    lang_config = get_lang_config(lang_code)
    
    # Get the language-specific translations for UI text
    translations = get_translations(lang_code)

    structured = None
    raw = None
    
    # The initial letter to show, from the language's alphabet
    initial_letter = lang_config['alphabet'][0]

    if request.method == "POST":
        letter = request.form.get("letter", initial_letter)
        attempt = request.form.get("attempt", "").strip()
        
        # MODIFIED: Use keyword arguments to prevent the TypeError
        prompt = build_letter_prompt(
            letter=letter,
            language_name=lang_config['name'],
            learner_attempt=attempt
        )
        
        raw = call_gemma_cli(prompt)
        try:
            structured = json.loads(raw.strip().split("\n")[-1])
        except Exception:
            structured = {"error": raw}
        log_vocab_attempt(f"Letter {letter}", attempt, {**structured, "level": "A", "lang": lang_code})

    return render_template(
        "letter.html",
        structured=structured,
        raw=raw,
        letter=request.form.get("letter", initial_letter),
        attempt=request.form.get("attempt", ""),
        lang_config=lang_config,
        lang_code=lang_code,
        t=translations
    )

@bp.route("/letter_sound")
def letter_sound():
    """Provides the text-to-speech string for a given letter and language."""
    lang_code = request.args.get('lang', 'en')
    letter = request.args.get('letter', 'A')
    
    # This could be expanded with more detailed lookups later
    speak_text = f"This is the letter {letter}."
    if lang_code == 'ar':
        speak_text = f"هذا حرف {letter}"
    elif lang_code == 'prs': # Dari (Persian)
        speak_text = f"این حرف {letter} است"

    return jsonify({"speak_text": speak_text})
