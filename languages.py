# A centralized place to manage language configurations

LANGUAGES = {
    "en": {
        "name": "English",
        "code": "en-US",
        "direction": "ltr", # Left-to-Right
        "alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "font": "'Nunito', system-ui, sans-serif",
        "sample_fonts": [
            "'Nunito', sans-serif",
            "'Georgia', serif",
            "'Courier New', monospace",
            "'Roboto Slab', serif"
        ]
    },
    "ar": {
        "name": "Arabic",
        "code": "ar-SA",
        "direction": "rtl", # Right-to-Left
        "alphabet": "أبتثجحخدذرزسشصضطظعغفقكلمنهوي",
        "font": "'Noto Naskh Arabic', serif",
        "sample_fonts": [
            "'Noto Naskh Arabic', serif",
            "'Amiri', serif",
            "'Lateef', cursive",
            "'Cairo', sans-serif"
        ]
    },
    "prs": {
        "name": "Dari",
        "code": "fa-AF",
        "direction": "rtl",
        "alphabet": "ابپتثجچحخدذرزژسشصضطظعغفقکگلمنهوی",
        "font": "'Noto Naskh Arabic', serif",
        "sample_fonts": [
            "'Noto Naskh Arabic', serif",
            "'Amiri', serif",
            "'Lateef', cursive",
            "'Cairo', sans-serif"
        ]
    }
}

STORY_IMAGES = {
    "en": [
        {"id": "apple", "file": "apple.jpg", "name": "Apple"},
        {"id": "ball", "file": "ball.jpg", "name": "Ball"},
        {"id": "car", "file": "car.jpg", "name": "Car"},
        {"id": "dog", "file": "dog.jpg", "name": "Dog"},
        {"id": "hat", "file": "hat.jpg", "name": "Hat"},
        {"id": "sun", "file": "sun.jpg", "name": "Sun"},
    ],
    "ar": [
        {"id": "apple", "file": "apple.jpg", "name": "تفاحة"},
        {"id": "ball", "file": "ball.jpg", "name": "كرة"},
        {"id": "car", "file": "car.jpg", "name": "سيارة"},
        {"id": "dog", "file": "dog.jpg", "name": "كلب"},
        {"id": "hat", "file": "hat.jpg", "name": "قبعة"},
        {"id": "sun", "file": "sun.jpg", "name": "شمس"},
    ],
    "prs": [
        {"id": "apple", "file": "apple.jpg", "name": "سیب"},
        {"id": "ball", "file": "ball.jpg", "name": "توپ"},
        {"id": "car", "file": "car.jpg", "name": "موتر"},
        {"id": "dog", "file": "dog.jpg", "name": "سگ"},
        {"id": "hat", "file": "hat.jpg", "name": "کلاه"},
        {"id": "sun", "file": "sun.jpg", "name": "آفتاب"},
    ]
}

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

# NEW: Data for the detailed letter lessons
LETTER_LESSONS = {
    "en": {
        "A": {
            "intro": "The letter 'A' is the first letter of the alphabet! It's a vowel and makes many cool sounds.",
            "phonemes": [
                {"symbol": "/æ/", "example": "cat"},
                {"symbol": "/eɪ/", "example": "cake"},
                {"symbol": "/ɒ/", "example": "watch"}
            ],
            "words": [
                {"word": "Apple", "example_sentence": "An apple a day keeps the doctor away."},
                {"word": "Ant", "example_sentence": "The tiny ant is carrying a big leaf."}
            ]
        }
        # ... You would add data for 'B', 'C', etc. here
    },
    "ar": {
        "أ": {
            "intro": "حرف 'الألف' هو أول حرف في الأبجدية! إنه حرف علة ويصدر العديد من الأصوات الرائعة.",
            "phonemes": [
                {"symbol": "/a/", "example": "أرنب"},
                {"symbol": "/aː/", "example": "باب"}
            ],
            "words": [
                {"word": "أسد", "example_sentence": "الأسد هو ملك الغابة."},
                {"word": "أزرق", "example_sentence": "السماء لونها أزرق."}
            ]
        }
        # ... Data for 'ب', 'ت', etc.
    },
    "prs": {
        "ا": {
            "intro": "حرف 'الف' اولین حرف الفبا است! این یک حرف صدادار است و صداهای جالب زیادی تولید می کند.",
            "phonemes": [
                {"symbol": "/ɑː/", "example": "آب"},
                {"symbol": "/a/", "example": "ابر"}
            ],
            "words": [
                {"word": "اسب", "example_sentence": "اسب حیوانی نجیب است."},
                {"word": "آسمان", "example_sentence": "آسمان آبی و زیبا است."}
            ]
        }
        # ... Data for 'ب', 'پ', etc.
    }
}

TRANSLATIONS = {
    "en": {
        "go_to_lesson_button": "Go to Lesson for '{letter}'",
        "back_to_home": "Back to Home",
        "tutors_voice": "Tutor's Voice",
        "teachers_feedback": "Teacher's Feedback",
        "feedback_header": "AI Feedback",
        "hear_feedback_button": "Hear Feedback",
        "read_aloud_button": "Read it for me",
        # --- Letter Practice & Lesson ---
        "letter_practice": "Letter Practice",
        "practice_typing": "Practice Typing",
        "selected_letter": "Selected Letter",
        "check_my_typing": "Check My Typing!",
        "letter_lesson_title": "Letter Lesson",
        "start_practice_button": "Practice Typing for '{letter}'",
        "learn_about_header": "Let's Learn About '{letter}'",
        "play_intro_button": "Play Intro",
        "see_the_letter_header": "See the Letter",
        "how_it_looks_text": "This is how the letter looks. The red one is the one we are learning!",
        "hear_sounds_header": "Hear the Sounds",
        "sounds_intro_text": "This letter can make different sounds. Let's listen!",
        "as_in_text": "as in",
        "play_sound_button": "Play",
        "practice_sounds_header": "Practice the Sounds",
        "sound_text": "Sound",
        "play_instruction_button": "Play Instruction",
        "your_attempt_label": "Your attempt (type here):",
        "record_voice_label": "Or record your voice:",
        "check_my_sound_button": "Check My Sound!",
        "practice_words_header": "Practice with Words",
        "word_text": "Word",
        "example_text": "Example",
        "check_my_word_button": "Check My Word!",
        "great_job_feedback": "Great job! 🎉",
        "good_try_feedback": "Good try! 👍",
        "play_feedback_button": "Play Feedback",
        # --- Word Pages ---
        "word_exercise_title": "Word Exercise",
        "choose_correct_word": "Choose the correct word for the image:",
        "correct_answer": "Correct!",
        "incorrect_answer": "Not quite, the correct answer was",
        "next_question": "Next Question",
        "word_lesson_title": "Word Lesson",
        "meaning_label": "Meaning",
        "syllables_label": "Syllables",
        "example_sentence_label": "Example Sentence",
        "hear_the_word_button": "Hear the Word",
        "next_word_button": "Next Word",
        "practice_exercises_button": "Practice Exercises",
        # --- Image Description ---
        "describe_image_title": "Describe an Image",
        "upload_an_image": "Upload an image to have the AI describe it:",
        "describe_button": "Describe Image",
        # --- Story Weaver ---
        "story_weaver_title": "Story Weaver",
        "story_instruction_1": "First, choose some pictures from the gallery.",
        "story_instruction_2": "Then, upload your own pictures if you like.",
        "story_instruction_3": "Finally, click the button to create your story!",
        "create_story_button": "Weave My Story!",
        "ai_story_header": "Here's Your Story!",
        "read_story_button": "Read it to Me",


    },
    "ar": {
        # --- Translations are incomplete, you would fill these in ---
        "go_to_lesson_button": "اذهب إلى درس '{letter}'",
        "back_to_home": "العودة إلى الرئيسية",
        "tutors_voice": "صوت المعلم",
        "teachers_feedback": "ملاحظات المعلم",
        "feedback_header": "تقييم الذكاء الاصطناعي",
        "hear_feedback_button": "اسمع التقييم",
        "read_aloud_button": "اقرأها لي",
        "letter_practice": "تمرين الحروف",
        "practice_typing": "أو تدرب على الكتابة",
        "selected_letter": "الحرف المختار",
        "check_my_typing": "تحقق من كتابتي!",
        "letter_lesson_title": "درس الحرف",
        "start_practice_button": "تدرب على كتابة '{letter}'",
        "learn_about_header": "لنتعلم عن '{letter}'",
        "play_intro_button": "تشغيل المقدمة",
        "see_the_letter_header": "شاهد الحرف",
        "how_it_looks_text": "هكذا يبدو الحرف. الحرف الأحمر هو الذي نتعلمه!",
        "hear_sounds_header": "اسمع الأصوات",
        "sounds_intro_text": "هذا الحرف يمكن أن يصدر أصواتًا مختلفة. هيا نستمع!",
        "as_in_text": "كما في",
        "play_sound_button": "تشغيل",
        "practice_sounds_header": "تدرب على الأصوات",
        "sound_text": "صوت",
        "play_instruction_button": "تشغيل التعليمات",
        "your_attempt_label": "محاولتك (اكتب هنا):",
        "record_voice_label": "أو سجل صوتك:",
        "check_my_sound_button": "تحقق من صوتي!",
        "practice_words_header": "تدرب على الكلمات",
        "word_text": "كلمة",
        "example_text": "مثال",
        "check_my_word_button": "تحقق من كلمتي!",
        "great_job_feedback": "عمل رائع! 🎉",
        "good_try_feedback": "محاولة جيدة! 👍",
        "play_feedback_button": "تشغيل التقييم",
        "word_exercise_title": "تمرين الكلمات",
        "choose_correct_word": "اختر الكلمة الصحيحة للصورة:",
        "correct_answer": "صحيح!",
        "incorrect_answer": "ليس تمامًا، الإجابة الصحيحة كانت",
        "next_question": "السؤال التالي",
        "word_lesson_title": "درس الكلمات",
        "meaning_label": "المعنى",
        "syllables_label": "المقاطع",
        "example_sentence_label": "جملة مثال",
        "hear_the_word_button": "اسمع الكلمة",
        "next_word_button": "الكلمة التالية",
        "practice_exercises_button": "تمارين عملية",
        "describe_image_title": "وصف صورة",
        "upload_an_image": "قم بتحميل صورة ليصفها الذكاء الاصطناعي:",
        "describe_button": "صف الصورة",
        "story_weaver_title": "حائك القصص",
        "story_instruction_1": "أولاً، اختر بعض الصور من المعرض.",
        "story_instruction_2": "بعد ذلك، قم بتحميل صورك الخاصة إذا أردت.",
        "story_instruction_3": "أخيرًا، انقر على الزر لإنشاء قصتك!",
        "create_story_button": "احبك قصتي!",
        "ai_story_header": "ها هي قصتك!",
        "read_story_button": "اقرأها لي",
    },
    "prs": {
        # --- Translations are incomplete, you would fill these in ---
        "go_to_lesson_button": "به درس '{letter}' بروید",
        "back_to_home": "بازگشت به خانه",
        "tutors_voice": "صدای معلم",
        "teachers_feedback": "بازخورد معلم",
        "feedback_header": "بازخورد هوش مصنوعی",
        "hear_feedback_button": "شنیدن بازخورد",
        "read_aloud_button": "برایم بخوان",
        "letter_practice": "تمرین حروف",
        "practice_typing": "یا تایپ کردن را تمرین کنید",
        "selected_letter": "حرف انتخاب شده",
        "check_my_typing": "تایپ من را بررسی کنید!",
        "letter_lesson_title": "درس حرف",
        "start_practice_button": "تمرین تایپ برای '{letter}'",
        "learn_about_header": "بیایید در مورد '{letter}' یاد بگیریم",
        "play_intro_button": "پخش مقدمه",
        "see_the_letter_header": "حرف را ببینید",
        "how_it_looks_text": "این شکلی است که حرف به نظر می رسد. قرمز آن چیزی است که ما یاد می گیریم!",
        "hear_sounds_header": "صداها را بشنوید",
        "sounds_intro_text": "این حرف می تواند صداهای مختلفی ایجاد کند. بیایید گوش کنیم!",
        "as_in_text": "مانند در",
        "play_sound_button": "پخش",
        "practice_sounds_header": "صداها را تمرین کنید",
        "sound_text": "صدا",
        "play_instruction_button": "پخش دستورالعمل",
        "your_attempt_label": "تلاش شما (اینجا تایپ کنید):",
        "record_voice_label": "یا صدای خود را ضبط کنید:",
        "check_my_sound_button": "صدای من را بررسی کنید!",
        "practice_words_header": "با کلمات تمرین کنید",
        "word_text": "کلمه",
        "example_text": "مثال",
        "check_my_word_button": "کلمه من را بررسی کنید!",
        "great_job_feedback": "آفرین! 🎉",
        "good_try_feedback": "تلاش خوبی بود! 👍",
        "play_feedback_button": "پخش بازخورد",
        "word_exercise_title": "تمرین کلمات",
        "choose_correct_word": "کلمه صحیح برای تصویر را انتخاب کنید:",
        "correct_answer": "درست است!",
        "incorrect_answer": "کاملاً درست نیست، جواب صحیح این بود",
        "next_question": "سوال بعدی",
        "word_lesson_title": "درس لغت",
        "meaning_label": "معنی",
        "syllables_label": "هجاها",
        "example_sentence_label": "جمله مثال",
        "hear_the_word_button": "کلمه را بشنوید",
        "next_word_button": "کلمه بعدی",
        "practice_exercises_button": "تمرین های عملی",
        "describe_image_title": "توصیف یک عکس",
        "upload_an_image": "یک عکس برای توصیف توسط هوش مصنوعی آپلود کنید:",
        "describe_button": "توصیف عکس",
        "story_weaver_title": "داستان باف",
        "story_instruction_1": "اول، چند عکس از گالری انتخاب کنید.",
        "story_instruction_2": "سپس، اگر دوست داشتید، عکس های خود را آپلود کنید.",
        "story_instruction_3": "در آخر، برای ساختن داستان خود، روی دکمه کلیک کنید!",
        "create_story_button": "داستانم را بباف!",
        "ai_story_header": "این داستان شماست!",
        "read_story_button": "برایم بخوان",
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

def get_story_images(lang_code='en'):
    """Returns the list of stock story images for a given language."""
    return STORY_IMAGES.get(lang_code, STORY_IMAGES['en'])
    
# NEW: Helper function for letter lessons
def get_letter_lesson(lang_code='en', letter='A'):
    """Returns the detailed lesson for a specific letter and language."""
    # Ensure letter matches the case in the dictionary (e.g., uppercase for English)
    letter_key = letter.upper() if lang_code == 'en' else letter
    lang_lessons = LETTER_LESSONS.get(lang_code, LETTER_LESSONS.get('en', {}))
    # Return the specific lesson, or a default empty lesson if not found
    return lang_lessons.get(letter_key, {"intro": "Lesson not found.", "phonemes": [], "words": []})
