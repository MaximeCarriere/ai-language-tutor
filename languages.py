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
        "practice_typing": "Or, Practice Typing",
        "selected_letter": "Selected Letter",
        "type_letter_here": "Type the letter here",
        "your_attempt": "Your attempt...",
        "check_my_typing": "Check My Typing!",
        "teachers_feedback": "Teacher's Feedback",
        "result": "Result",
        "correct": "Correct! 🎉",
        "not_quite": "Not quite, try again! 👍",
        "feedback": "Feedback",
        # --- New Translations for Drawing Page ---
        "letter_drawing_title": "Letter Drawing",
        "letter_to_practice": "Letter to Practice",
        "tutors_voice": "Tutor's Voice",
        "loading_voices": "Loading...",
        "clear_drawing": "Clear Drawing",
        "get_feedback": "Get Feedback!",
        "initial_instruction": "Let's draw! Pick a letter, draw it in the box, and click 'Get Feedback!'"
    },
    "ar": {
        "letter_practice": "تمرين الحروف",
        "back_to_home": "العودة إلى الرئيسية",
        "click_a_letter": "انقر على حرف!",
        "lets_go": "هيا بنا!",
        "learn_about_letter": "لنتعلم عن '{letter}'!",
        "practice_typing": "أو تدرب على الكتابة",
        "selected_letter": "الحرف المختار",
        "type_letter_here": "اكتب الحرف هنا",
        "your_attempt": "محاولتك...",
        "check_my_typing": "تحقق من كتابتي!",
        "teachers_feedback": "ملاحظات المعلم",
        "result": "النتيجة",
        "correct": "صحيح! 🎉",
        "not_quite": "ليس تماما حاول مرة أخرى! 👍",
        "feedback": "ملاحظات",
        # --- New Translations for Drawing Page ---
        "letter_drawing_title": "رسم الحروف",
        "letter_to_practice": "حرف للتمرين",
        "tutors_voice": "صوت المعلم",
        "loading_voices": "جار التحميل...",
        "clear_drawing": "مسح الرسم",
        "get_feedback": "احصل على ملاحظات!",
        "initial_instruction": "هيا نرسم! اختر حرفًا، ارسمه في المربع، وانقر على 'احصل على ملاحظات!'"
    },
    "prs": {
        "letter_practice": "تمرین حروف",
        "back_to_home": "بازگشت به خانه",
        "click_a_letter": "روی یک حرف کلیک کنید!",
        "lets_go": "بزن بریم!",
        "learn_about_letter": "بیایید در مورد '{letter}' یاد بگیریم!",
        "practice_typing": "یا تایپ کردن را تمرین کنید",
        "selected_letter": "حرف انتخاب شده",
        "type_letter_here": "حرف را اینجا تایپ کنید",
        "your_attempt": "تلاش شما...",
        "check_my_typing": "تایپ من را بررسی کنید!",
        "teachers_feedback": "بازخورد معلم",
        "result": "نتیجه",
        "correct": "درست است! 🎉",
        "not_quite": "کاملاً درست نیست، دوباره امتحان کنید! 👍",
        "feedback": "بازخورد",
        # --- New Translations for Drawing Page ---
        "letter_drawing_title": "ترسیم حروف",
        "letter_to_practice": "حرف برای تمرین",
        "tutors_voice": "صدای معلم",
        "loading_voices": "در حال بارگذاری...",
        "clear_drawing": "پاک کردن طرح",
        "get_feedback": "دریافت بازخورد!",
        "initial_instruction": "بیایید نقاشی کنیم! یک حرف را انتخاب کنید، آن را در کادر بکشید و روی 'دریافت بازخورد!' کلیک کنید."
    }
}

def get_lang_config(lang_code='en'):
    """Returns the configuration for a given language code."""
    return LANGUAGES.get(lang_code, LANGUAGES['en'])

def get_translations(lang_code='en'):
    """Returns the translations for a given language code."""
    return TRANSLATIONS.get(lang_code, TRANSLATIONS['en'])
