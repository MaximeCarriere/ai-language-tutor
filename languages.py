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

TRANSLATIONS = {
    "en": {
        # --- General & Letter Pages ---
        "letter_practice": "Letter Practice",
        "back_to_home": "Back to Home",
        "practice_typing": "Practice Typing",
        "selected_letter": "Selected Letter",
        "teachers_feedback": "Teacher's Feedback",
        "correct": "Correct! 🎉",
        "not_quite": "Not quite, try again! 👍",
        # --- Drawing Page ---
        "letter_drawing_title": "Letter Drawing",
        "tutors_voice": "Tutor's Voice",
        # --- Word Exercise Page ---
        "word_exercise_title": "Word Exercise",
        "choose_correct_word": "Choose the correct word for the image:",
        "correct_answer": "Correct!",
        "incorrect_answer": "Not quite, the correct answer was",
        "next_question": "Next Question",
        # --- Word Lesson Page ---
        "word_lesson_title": "Word Lesson",
        "meaning_label": "Meaning",
        "syllables_label": "Syllables",
        "example_sentence_label": "Example Sentence",
        "hear_the_word_button": "Hear the Word",
        "next_word_button": "Next Word",
        "practice_exercises_button": "Practice Exercises",
        # --- Image Description Page ---
        "describe_image_title": "Describe an Image",
        "upload_an_image": "Upload an image to have the AI describe it:",
        "describe_button": "Describe Image",
        "feedback_header": "AI Feedback",
        "hear_feedback_button": "Hear Feedback",
        "read_aloud_button": "Read it for me",
        # --- Story Weaver Page ---
        "story_weaver_title": "Story Weaver",
        "story_instruction_1": "First, choose some pictures from the gallery.",
        "story_instruction_2": "Then, upload your own pictures if you like.",
        "story_instruction_3": "Finally, click the button to create your story!",
        "create_story_button": "Weave My Story!",
        "ai_story_header": "Here's Your Story!",
        "read_story_button": "Read it to Me"
    },
    "ar": {
        # --- General & Letter Pages ---
        "letter_practice": "تمرين الحروف",
        "back_to_home": "العودة إلى الرئيسية",
        "practice_typing": "أو تدرب على الكتابة",
        "selected_letter": "الحرف المختار",
        "teachers_feedback": "ملاحظات المعلم",
        "correct": "صحيح! 🎉",
        "not_quite": "ليس تماما حاول مرة أخرى! 👍",
        # --- Drawing Page ---
        "letter_drawing_title": "رسم الحروف",
        "tutors_voice": "صوت المعلم",
        # --- Word Exercise Page ---
        "word_exercise_title": "تمرين الكلمات",
        "choose_correct_word": "اختر الكلمة الصحيحة للصورة:",
        "correct_answer": "صحيح!",
        "incorrect_answer": "ليس تمامًا، الإجابة الصحيحة كانت",
        "next_question": "السؤال التالي",
        # --- Word Lesson Page ---
        "word_lesson_title": "درس الكلمات",
        "meaning_label": "المعنى",
        "syllables_label": "المقاطع",
        "example_sentence_label": "جملة مثال",
        "hear_the_word_button": "اسمع الكلمة",
        "next_word_button": "الكلمة التالية",
        "practice_exercises_button": "تمارين عملية",
        # --- Image Description Page ---
        "describe_image_title": "وصف صورة",
        "upload_an_image": "قم بتحميل صورة ليصفها الذكاء الاصطناعي:",
        "describe_button": "صف الصورة",
        "feedback_header": "تقييم الذكاء الاصطناعي",
        "hear_feedback_button": "اسمع التقييم",
        "read_aloud_button": "اقرأها لي",
        # --- Story Weaver Page ---
        "story_weaver_title": "حائك القصص",
        "story_instruction_1": "أولاً، اختر بعض الصور من المعرض.",
        "story_instruction_2": "بعد ذلك، قم بتحميل صورك الخاصة إذا أردت.",
        "story_instruction_3": "أخيرًا، انقر على الزر لإنشاء قصتك!",
        "create_story_button": "احبك قصتي!",
        "ai_story_header": "ها هي قصتك!",
        "read_story_button": "اقرأها لي"
    },
    "prs": {
        # --- General & Letter Pages ---
        "letter_practice": "تمرین حروف",
        "back_to_home": "بازگشت به خانه",
        "practice_typing": "یا تایپ کردن را تمرین کنید",
        "selected_letter": "حرف انتخاب شده",
        "teachers_feedback": "بازخورد معلم",
        "correct": "درست است! 🎉",
        "not_quite": "کاملاً درست نیست، دوباره امتحان کنید! 👍",
        # --- Drawing Page ---
        "letter_drawing_title": "ترسیم حروف",
        "tutors_voice": "صدای معلم",
        # --- Word Exercise Page ---
        "word_exercise_title": "تمرین کلمات",
        "choose_correct_word": "کلمه صحیح برای تصویر را انتخاب کنید:",
        "correct_answer": "درست است!",
        "incorrect_answer": "کاملاً درست نیست، جواب صحیح این بود",
        "next_question": "سوال بعدی",
        # --- Word Lesson Page ---
        "word_lesson_title": "درس لغت",
        "meaning_label": "معنی",
        "syllables_label": "هجاها",
        "example_sentence_label": "جمله مثال",
        "hear_the_word_button": "کلمه را بشنوید",
        "next_word_button": "کلمه بعدی",
        "practice_exercises_button": "تمرین های عملی",
        # --- Image Description Page ---
        "describe_image_title": "توصیف یک عکس",
        "upload_an_image": "یک عکس برای توصیف توسط هوش مصنوعی آپلود کنید:",
        "describe_button": "توصیف عکس",
        "feedback_header": "بازخورد هوش مصنوعی",
        "hear_feedback_button": "شنیدن بازخورد",
        "read_aloud_button": "برایم بخوان",
        # --- Story Weaver Page ---
        "story_weaver_title": "داستان باف",
        "story_instruction_1": "اول، چند عکس از گالری انتخاب کنید.",
        "story_instruction_2": "سپس، اگر دوست داشتید، عکس های خود را آپلود کنید.",
        "story_instruction_3": "در آخر، برای ساختن داستان خود، روی دکمه کلیک کنید!",
        "create_story_button": "داستانم را بباف!",
        "ai_story_header": "این داستان شماست!",
        "read_story_button": "برایم بخوان"
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
