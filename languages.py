# A centralized place to manage language configurations

LANGUAGES = {
    "en": {
        "name": "English",
        "code": "en-US",
        "direction": "ltr", # Left-to-Right
        "alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "font": "'Nunito', system-ui, sans-serif"
    },
    "ar": {
        "name": "Arabic",
        "code": "ar-SA",
        "direction": "rtl", # Right-to-Left
        "alphabet": "أبتثجحخدذرزسشصضطظعغفقكلمنهوي",
        "font": "'Noto Naskh Arabic', serif"
    },
    "prs": {
        "name": "Dari",
        "code": "fa-AF",
        "direction": "rtl",
        "alphabet": "ابپتثجچحخدذرزژسشصضطظعغفقکگلمنهوی",
        "font": "'Noto Naskh Arabic', serif"
    }
}

TRANSLATIONS = {
    "en": {
        "letter_practice": "Letter Practice",
        "back_to_home": "Back to Home",
        "click_a_letter": "Click a Letter!",
        "lets_go": "Let's Go!",
        "learn_about_letter": "Let's learn about '{letter}'!",
        "practice_typing": "Practice Typing",
        "selected_letter": "Selected Letter",
        "type_letter_here": "Type the letter here",
        "your_attempt": "Your attempt...",
        "check_my_typing": "Check My Typing!",
        "teachers_feedback": "Teacher's Feedback",
        "result": "Result",
        "correct": "Correct! 🎉",
        "not_quite": "Not quite, try again! 👍",
        "feedback": "Feedback",
        # --- Translations for Drawing Page ---
        "letter_drawing_title": "Letter Drawing",
        "letter_to_practice": "Letter to Practice",
        "tutors_voice": "Tutor's Voice",
        "loading_voices": "Loading...",
        "clear_drawing": "Clear Drawing",
        "get_feedback": "Get Feedback!",
        "initial_instruction": "Let's draw! Pick a letter, draw it in the box, and click 'Get Feedback!'",
        # --- Translations for Word Exercise ---
        "word_exercise_title": "Word Exercise",
        "choose_correct_word": "Choose the correct word for the image:",
        "correct_answer": "Correct!",
        "incorrect_answer": "Not quite, the correct answer was",
        "next_question": "Next Question",
        # --- ADDED: Translations for Word Lesson ---
        "word_lesson_title": "Word Lesson",
        "meaning_label": "Meaning",
        "syllables_label": "Syllables",
        "example_sentence_label": "Example Sentence",
        "hear_the_word_button": "Hear the Word",
        "next_word_button": "Next Word",
        "practice_exercises_button": "Practice Exercises",
        
        # --- Translations for Vocabulary Practice Page ---
        "vocab_practice_title": "Vocabulary Practice",
        "image_label": "Image of an object:",
        "speak_or_type_label": "Speak or type what you see:",
        "type_if_no_audio_placeholder": "Type description here...",
        "upload_voice_label": "Or upload a voice recording:",
        "practice_button": "Get Feedback",
        "feedback_header": "AI Feedback",
        "hear_feedback_button": "Hear Feedback",
        
        # Translations for Image Description Page ---
        "describe_image_title": "Describe an Image",
        "upload_an_image": "Upload an image to have the AI describe it:",
        "describe_button": "Describe Image",
        "read_aloud_button": "Read it for me"
    },
    "ar": {
        "letter_practice": "تمرين الحروف",
        "back_to_home": "العودة إلى الرئيسية",
        # ... (all other existing ar translations) ...
        "initial_instruction": "هيا نرسم! اختر حرفًا، ارسمه في المربع، وانقر على 'احصل على ملاحظات!'",
        # --- Translations for Word Exercise ---
        "word_exercise_title": "تمرين الكلمات",
        "choose_correct_word": "اختر الكلمة الصحيحة للصورة:",
        "correct_answer": "صحيح!",
        "incorrect_answer": "ليس تمامًا، الإجابة الصحيحة كانت",
        "next_question": "السؤال التالي",
        # --- ADDED: Translations for Word Lesson ---
        "word_lesson_title": "درس الكلمات",
        "meaning_label": "المعنى",
        "syllables_label": "المقاطع",
        "example_sentence_label": "جملة مثال",
        "hear_the_word_button": "اسمع الكلمة",
        "next_word_button": "الكلمة التالية",
        "practice_exercises_button": "تمارين عملية"
    },
    "prs": {
        "letter_practice": "تمرین حروف",
        "back_to_home": "بازگشت به خانه",
        # ... (all other existing prs translations) ...
        "initial_instruction": "بیایید نقاشی کنیم! یک حرف را انتخاب کنید، آن را در کادر بکشید و روی 'دریافت بازخورد!' کلیک کنید.",
        # --- Translations for Word Exercise ---
        "word_exercise_title": "تمرین کلمات",
        "choose_correct_word": "کلمه صحیح برای تصویر را انتخاب کنید:",
        "correct_answer": "درست است!",
        "incorrect_answer": "کاملاً درست نیست، جواب صحیح این بود",
        "next_question": "سوال بعدی",
        # --- ADDED: Translations for Word Lesson ---
        "word_lesson_title": "درس لغت",
        "meaning_label": "معنی",
        "syllables_label": "هجاها",
        "example_sentence_label": "جمله مثال",
        "hear_the_word_button": "کلمه را بشنوید",
        "next_word_button": "کلمه بعدی",
        "practice_exercises_button": "تمرین های عملی"
    }
}

# REPLACED: This data now includes full details for the lesson page.
VOCABULARY_DATA = {
    "en": {
        "exercises": [
            {"image": "apple.jpg", "word": "Apple", "syllables": "Ap-ple", "meaning": "A round fruit with firm, white flesh and a green or red skin.", "example_sentence": "I ate an apple for a snack."},
            {"image": "car.jpg", "word": "Car", "syllables": "Car", "meaning": "A road vehicle, typically with four wheels, powered by an internal combustion engine or electric motor.", "example_sentence": "The car is parked in the garage."},
            {"image": "sun.jpg", "word": "Sun", "syllables": "Sun", "meaning": "The star around which the earth orbits, providing light and heat.", "example_sentence": "The sun is very bright today."}
        ],
        "distractors": ["Cat", "Box", "Cup", "Key", "Map", "Pen", "Star", "Tree"]
    },
    "ar": {
        "exercises": [
            {"image": "apple.jpg", "word": "تفاحة", "syllables": "تف-فا-حة", "meaning": "ثمرة دائرية ذات لحم أبيض متماسك وقشرة خضراء أو حمراء.", "example_sentence": "أكلت تفاحة كوجبة خفيفة."},
            {"image": "car.jpg", "word": "سيارة", "syllables": "سي-يا-رة", "meaning": "مركبة طرق، عادة بأربع عجلات، تعمل بمحرك احتراق داخلي أو محرك كهربائي.", "example_sentence": "السيارة متوقفة في المرآب."},
            {"image": "sun.jpg", "word": "شمس", "syllables": "شمس", "meaning": "النجم الذي تدور حوله الأرض، ويوفر الضوء والحرارة.", "example_sentence": "الشمس مشرقة جدا اليوم."}
        ],
        "distractors": ["قطة", "صندوق", "كوب", "مفتاح", "خريطة", "قلم", "نجمة", "شجرة"]
    },
    "prs": {
        "exercises": [
            {"image": "apple.jpg", "word": "سیب", "syllables": "سیب", "meaning": "یک میوه گرد با گوشت سفید و سفت و پوست سبز یا سرخ.", "example_sentence": "من برای میان وعده یک سیب خوردم."},
            {"image": "car.jpg", "word": "موتر", "syllables": "مو-تر", "meaning": "یک وسیله نقلیه جاده ای، معمولاً با چهار چرخ، که توسط موتور احتراق داخلی یا موتور الکتریکی کار می کند.", "example_sentence": "موتر در گاراژ پارک شده است."},
            {"image": "sun.jpg", "word": "آفتاب", "syllables": "آف-تاب", "meaning": "ستاره ای که زمین به دور آن می چرخد و نور و گرما را تأمین می کند.", "example_sentence": "امروز آفتاب بسیار روشن است."}
        ],
        "distractors": ["پشک", "جعبه", "پیاله", "کلید", "نقشه", "قلم", "ستاره", "درخت"]
    }
}


def get_lang_config(lang_code='en'):
    """Returns the configuration for a given language code."""
    return LANGUAGES.get(lang_code, LANGUAGES['en'])

def get_translations(lang_code='en'):
    """Returns the translations for a given language code."""
    return TRANSLATIONS.get(lang_code, TRANSLATIONS['en'])

def get_vocabulary_data(lang_code='en'):
    """Returns the exercises and distractors for a given language."""
    return VOCABULARY_DATA.get(lang_code, VOCABULARY_DATA['en'])
