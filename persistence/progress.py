# persistence/progress.py
import os
import json
from datetime import datetime

DATA_DIR = "data"
PROGRESS_FILE = os.path.join(DATA_DIR, "progress.json")

def _ensure_dirs():
    os.makedirs(DATA_DIR, exist_ok=True)

def _load_progress():
    _ensure_dirs()
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "r") as f:
            return json.load(f)
    return {"vocab": [], "describe": [], "math": []}

def _save_progress(data):
    _ensure_dirs()
    with open(PROGRESS_FILE, "w") as f:
        json.dump(data, f, indent=2)

def log_vocab_attempt(description, transcription, structured):
    data = _load_progress()
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "description": description,
        "transcription": transcription,
        "result": structured,
    }
    data.setdefault("vocab", []).append(entry)
    _save_progress(data)

def log_description_attempt(structured):
    data = _load_progress()
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "result": structured,
    }
    data.setdefault("describe", []).append(entry)
    _save_progress(data)

def log_math_attempt(question, structured):
    data = _load_progress()
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "question": question,
        "result": structured,
    }
    data.setdefault("math", []).append(entry)
    _save_progress(data)
