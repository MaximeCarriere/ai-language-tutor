# routes/sentences.py

from flask import Blueprint, render_template, request
from languages import get_lang_config, get_translations

bp = Blueprint("sentences", __name__, template_folder="../templates")

@bp.route("/")
def sentences_hub():
    """Renders the main hub for all sentence-level activities."""
    lang_code = request.args.get('lang', 'en')
    lang_config = get_lang_config(lang_code)
    translations = get_translations(lang_code)

    return render_template(
        "sentences.html",
        lang_config=lang_config,
        lang_code=lang_code,
        t=translations
    )
