import random
# MODIFIED: Import 'request' and our language helper functions
from flask import Blueprint, render_template, request
from languages import get_lang_config, get_translations, get_vocabulary_data

bp = Blueprint("word_lesson", __name__, template_folder="../templates")


# REMOVED: The hard-coded English lesson list is no longer needed.
# This data now lives in the VOCABULARY_DATA dictionary in languages.py.


# MODIFIED: This function now gets a random lesson for a specific language.
def get_random_lesson(lang_code='en'):
    """Selects a random, detailed word lesson for the given language."""
    # Get all vocabulary data for the specified language.
    vocab = get_vocabulary_data(lang_code)
    
    # The 'exercises' list in our data contains the detailed lesson info.
    # We just need to pick one to be our lesson for this page.
    lesson = random.choice(vocab["exercises"])
    
    # Construct the full URL for the image and add it to the dictionary.
    lesson["image_url"] = f"/static/images/{lesson['image']}"
    return lesson


# MODIFIED: The route now handles the language parameter and passes all necessary data.
@bp.route("/")
def show_lesson():
    """Renders the detailed word lesson page."""
    # Get the language from the URL, e.g., /word_lesson?lang=ar
    lang_code = request.args.get('lang', 'en')
    
    # Load all data required by the template for this language.
    lang_config = get_lang_config(lang_code)
    translations = get_translations(lang_code)
    lesson_data = get_random_lesson(lang_code)
    
    # Pass everything to the template for rendering.
    return render_template(
        "word_lesson.html",
        lesson=lesson_data,
        lang_config=lang_config,
        lang_code=lang_code,
        t=translations
    )
