import json
import os
from datetime import datetime

PROGRESS_FILE = "data/progress.json"

def _load():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE) as f:
            return json.load(f)
    return {"vocab": [], "math": []}

def _save(data):
    with open(PROGRESS_FILE, "w") as f:
        json.dump(data, f, indent=2)

def log_vocab_attempt(description, transcription, structured):
    data = _load()
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "description": description,
        "transcription": transcription,
        "result": structured,
    }
    data["vocab"].append(entry)
    _save(data)

def log_math_attempt(question, structured):
    data = _load()
    entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "question": question,
        "result": structured,
    }
    data["math"].append(entry)
    _save(data)
