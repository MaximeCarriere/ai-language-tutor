import random
from flask import Blueprint, render_template

bp = Blueprint("word_exercise", __name__, template_folder="../templates")

# For this example, we'll create a simple list of exercises.
# In a real app, this could come from a database.
# NOTE: You must have these images in your `static/images/` folder.
WORD_EXERCISES = [
    {"image": "apple.jpg", "word": "Apple"},
    {"image": "ball.jpg", "word": "Ball"},
    {"image": "car.jpg", "word": "Car"},
    {"image": "dog.jpg", "word": "Dog"},
    {"image": "hat.jpg", "word": "Hat"},
    {"image": "sun.jpg", "word": "Sun"},
]

# A pool of incorrect words to use as distractors.
DISTRACTOR_WORDS = ["Cat", "Box", "Cup", "Key", "Map", "Pen", "Star", "Tree"]

def generate_word_exercise():
    """Selects a random exercise and generates multiple-choice options."""
    # Choose a random exercise
    exercise = random.choice(WORD_EXERCISES)
    correct_word = exercise["word"]

    # Generate distractor choices
    choices = {correct_word}
    while len(choices) < 4:
        distractor = random.choice(DISTRACTOR_WORDS)
        if distractor != correct_word:
            choices.add(distractor)

    # Shuffle the choices
    shuffled_choices = list(choices)
    random.shuffle(shuffled_choices)

    return {
        "image_url": f"/static/images/{exercise['image']}",
        "choices": shuffled_choices,
        "correct_word": correct_word,
    }

@bp.route("/")
def show_exercise():
    """Renders a single word exercise page."""
    exercise_data = generate_word_exercise()
    return render_template("word_exercise.html", exercise=exercise_data)
