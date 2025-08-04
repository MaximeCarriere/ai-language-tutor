import random
from flask import Blueprint, render_template

bp = Blueprint("word_lesson", __name__, template_folder="../templates")

# This is your new "database" of word lessons.
# Make sure you have these images in a `static/images/` folder.
WORD_LESSONS = [
    {
        "word": "Apple",
        "image": "apple.jpg",
        "syllables": "Ap-ple",
        "meaning": "A round fruit with red or green skin and a crisp texture.",
        "example_sentence": "I like to eat an apple for a snack."
    },
    {
        "word": "Ball",
        "image": "ball.jpg",
        "syllables": "Ball",
        "meaning": "A round object used in games and sports.",
        "example_sentence": "The boy threw the red ball."
    },
    {
        "word": "Car",
        "image": "car.jpg",
        "syllables": "Car",
        "meaning": "A road vehicle, typically with four wheels, powered by an engine.",
        "example_sentence": "The car is driving down the street."
    },
    {
        "word": "Dog",
        "image": "dog.jpg",
        "syllables": "Dog",
        "meaning": "A domesticated animal with four legs, a tail, and fur.",
        "example_sentence": "The dog likes to play fetch."
    },
    {
        "word": "Sun",
        "image": "sun.jpg",
        "syllables": "Sun",
        "meaning": "The star that provides light and heat to the Earth.",
        "example_sentence": "The sun is bright and yellow."
    }
]

def get_word_lesson():
    """Selects a random lesson and prepares its data for the template."""
    lesson = random.choice(WORD_LESSONS)
    # Construct the full URL for the image
    lesson["image_url"] = f"/static/images/{lesson['image']}"
    return lesson

# --- CORRECTED CODE ---
# Add a route for "" (which corresponds to /word_lesson)
@bp.route("")
@bp.route("/")
def show_lesson():
    """Renders a single word lesson page."""
    lesson_data = get_word_lesson()
    return render_template("word_lesson.html", lesson=lesson_data)
