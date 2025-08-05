import random
# MODIFIED: Import 'request' and our language helper functions
from flask import Blueprint, render_template, request
from languages import get_lang_config, get_translations, get_vocabulary_data

bp = Blueprint("word_exercise", __name__, template_folder="../templates")


# REMOVED: The hard-coded English word lists are no longer needed here.
# They now live inside the VOCABULARY_DATA dictionary in languages.py.


# MODIFIED: The function now requires a lang_code to get the correct words.
def generate_word_exercise(lang_code='en'):
    """Selects a random exercise and generates multiple-choice options for a given language."""
    # MODIFIED: Get the vocabulary for the specified language from our helper.
    vocab = get_vocabulary_data(lang_code)
    word_exercises = vocab["exercises"]
    distractor_words = vocab["distractors"]

    # Choose a random exercise
    exercise = random.choice(word_exercises)
    correct_word = exercise["word"]

    # Generate distractor choices from the correct language's pool.
    # This logic is also improved to prevent errors if not enough distractors exist.
    choices = {correct_word}
    distractor_pool = [d for d in distractor_words if d != correct_word]
    random.shuffle(distractor_pool)
    
    while len(choices) < 4 and distractor_pool:
        choices.add(distractor_pool.pop())

    # Shuffle the final choices
    shuffled_choices = list(choices)
    random.shuffle(shuffled_choices)

    return {
        "image_url": f"/static/images/{exercise['image']}",
        "choices": shuffled_choices,
        "correct_word": correct_word,
    }

# MODIFIED: The route now handles the language parameter and passes all data.
@bp.route("/")
def show_exercise():
    """Renders a single word exercise page, aware of the selected language."""
    # Get language from URL query (e.g., /word_exercise?lang=ar), default to 'en'
    lang_code = request.args.get('lang', 'en')
    
    # Load all necessary language-specific data using our helpers
    lang_config = get_lang_config(lang_code)
    translations = get_translations(lang_code)
    exercise_data = generate_word_exercise(lang_code)
    
    # Pass everything to the template
    return render_template(
        "word_exercise.html",
        exercise=exercise_data,
        lang_config=lang_config,
        lang_code=lang_code,
        t=translations
    )
