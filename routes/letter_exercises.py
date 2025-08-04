import os
import random
from flask import Blueprint, render_template, request, current_app

# adjust if your templates live elsewhere; the app-level template folder should also cover this
letter_exercises_bp = Blueprint(
    "letter_exercises",
    __name__,
    template_folder=os.path.join(os.getcwd(), "templates"),
)

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# --- UPDATED: Expanded word list for more variety ---
SAMPLE_WORDS = [
    "apple", "apron", "anchor", "ant", "alarm", "art", "aunt",
    "ball", "banana", "book", "box", "bus", "boy",
    "cat", "car", "cup", "cake", "coat", "clock",
    "dog", "door", "desk", "duck", "doll", "drum",
    "ear", "egg", "elf", "eat", "end", "exit",
    "fan", "fish", "fox", "frog", "five", "foot",
    "grape", "girl", "goat", "gift", "go", "gem",
    "hat", "hen", "hand", "hill", "home", "hop",
    "ice", "igloo", "ink", "ill", "in", "its",
    "jet", "jar", "jug", "jump", "job", "joy",
    "key", "kite", "king", "kid", "kick", "keep",
    "lamp", "leg", "lion", "leaf", "lock", "log",
    "map", "man", "mop", "moon", "milk", "mix",
    "net", "nose", "nut", "nap", "nest", "nine",
    "owl", "orange", "on", "off", "one", "open",
    "pan", "pen", "pig", "pot", "pin", "pop",
    "queen", "quilt", "quiet", "quick", "quiz",
    "rat", "red", "run", "ring", "road", "rock",
    "sat", "sun", "six", "sit", "sock", "stop",
    "table", "ten", "top", "toy", "tub", "tie",
    "use", "up", "under", "urn",
    "van", "vet", "vase", "very",
    "web", "wet", "win", "wig",
    "box", "fox", "six", "wax",
    "yak", "yes", "yet", "yum", "you",
    "zip", "zoo", "zero", "zig"
]


def generate_letter_series(target_letter, count=5, series_len=5):
    series = []
    for _ in range(count):
        choices = []
        pos = random.randrange(series_len)
        for i in range(series_len):
            if i == pos:
                # mix case
                choices.append(random.choice([target_letter.upper(), target_letter.lower()]))
            else:
                other = random.choice([c for c in ALPHABET if c.upper() != target_letter.upper()])
                choices.append(random.choice([other.upper(), other.lower()]))
        series.append({"choices": choices, "correct_index": pos})
    return series

def generate_word_series_with_letter(target_letter, count=5, candidates_per_series=5):
    series = []
    for _ in range(count):
        # ensure there's at least one correct word
        valid = [w for w in SAMPLE_WORDS if target_letter.lower() in w.lower()]
        if not valid:
            # Fallback if no words contain the letter (unlikely with new list)
            correct = "apple" if target_letter.lower() == 'a' else 'dog'
        else:
            correct = random.choice(valid)
        
        others = []
        # --- UPDATED: Added a safeguard to prevent infinite loops ---
        attempts = 0
        max_attempts = 50  # Limit attempts to find words

        while len(others) < candidates_per_series - 1 and attempts < max_attempts:
            w = random.choice(SAMPLE_WORDS)
            attempts += 1 # always increment to prevent getting stuck
            
            # Condition to skip the word:
            # 1. It contains the target letter.
            # 2. It's already been added to the 'others' list.
            # 3. It's the same as the 'correct' word.
            if (target_letter.lower() in w.lower()) or w in others or w == correct:
                continue
                
            others.append(w)
        
        # If the loop finished due to max_attempts, log a warning
        if attempts >= max_attempts:
            current_app.logger.warning(
                f"Could not find enough words without letter '{target_letter}' after {max_attempts} attempts."
            )

        choices = others + [correct]
        random.shuffle(choices)
        correct_index = choices.index(correct)
        series.append({"choices": choices, "correct_index": correct_index})
    return series

@letter_exercises_bp.route("/debug")
def debug():
    letter = request.args.get("letter", "A").upper()
    current_app.logger.debug("Entered letter_exercise debug for letter=%s", letter)
    return render_template("letter_exercise.html", letter=letter, letter_recognition=[], word_finder=[])

@letter_exercises_bp.route("", methods=["GET"])
@letter_exercises_bp.route("/", methods=["GET"])
def letter_exercise():
    letter = request.args.get("letter", "A").upper() or "A"
    current_app.logger.debug("entering letter_exercise for letter=%s", letter)
    # Hardcode fallback to "A" if something is off
    if not letter.isalpha() or len(letter) != 1:
        current_app.logger.warning("Invalid letter '%s', falling back to 'A'", letter)
        letter = "A"

    # Generate series
    letter_recognition = generate_letter_series(letter)
    word_finder = generate_word_series_with_letter(letter)
    current_app.logger.debug("Generated letter_recognition and word_finder for %s", letter)

    return render_template(
        "letter_exercise.html",
        letter=letter,
        letter_recognition=letter_recognition,
        word_finder=word_finder,
    )
