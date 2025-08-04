import re, json, html

_ansi_re = re.compile(r'\x1B[@-_][0-?]*[ -/]*[@-~]')

def fix_mojibake(s: str) -> str:
    try:
        return s.encode("latin1").decode("utf-8")
    except Exception:
        return s

def clean_unicode_escapes(s: str) -> str:
    try:
        return bytes(s, "utf-8").decode("unicode_escape")
    except Exception:
        return s

def normalize_feedback(raw: str) -> str:
    clean = _ansi_re.sub("", raw)
    if "[stderr]" in clean:
        clean = clean.split("[stderr]")[0]
    clean = clean.strip()

    feedback = ""
    try:
        parsed = json.loads(clean)
        for key in ("feedback", "pronunciation_feedback", "next_prompt"):
            if key in parsed and isinstance(parsed[key], str) and parsed[key].strip():
                feedback = parsed[key].strip()
                break
        if not feedback:
            for v in parsed.values():
                if isinstance(v, str) and v.strip():
                    feedback = v.strip()
                    break
    except Exception:
        feedback = clean

    feedback = fix_mojibake(feedback)
    feedback = clean_unicode_escapes(feedback)
    feedback = html.unescape(feedback)
    feedback = feedback.replace("’", "'").replace("“", '"').replace("”", '"')
    feedback = " ".join(feedback.split())
    return feedback
