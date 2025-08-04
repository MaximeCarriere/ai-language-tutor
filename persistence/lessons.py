import json

LETTER_LESSON_FILE = "letter_lessons.json"
LETTER_DATA_FILE = "letter_data.json"

def load_letter_lesson(letter):
    try:
        with open(LETTER_LESSON_FILE) as f:
            lessons = json.load(f)
        return lessons.get(letter.upper(), {})
    except FileNotFoundError:
        return {}

def load_letter_info(letter):
    try:
        with open(LETTER_DATA_FILE) as f:
            data = json.load(f)
        return data.get(letter.upper(), {}).get("sound", ""), data.get(letter.upper(), {}).get("example_word", "")
    except FileNotFoundError:
        return "", ""
