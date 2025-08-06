# routes/words.py

from flask import Blueprint, render_template, request
from languages import get_lang_config, get_translations

# This blueprint serves the main hub page for all word-related activities
bp = Blueprint("words", __name__, template_folder="../templates")

@bp.route("/")
def words_hub():
    """Renders the main words hub page."""
    lang_code = request.args.get('lang', 'en')
    lang_config = get_lang_config(lang_code)
    translations = get_translations(lang_code)

    return render_template(
        "words.html",
        lang_config=lang_config,
        lang_code=lang_code,
        t=translations
    )
