from flask import Blueprint, render_template, request
from services.ollama import is_ollama_up, gemma_health_check, call_gemma_cli
from persistence.progress import log_vocab_attempt
from prompts import build_vocab_prompt
import os

bp = Blueprint("vocab", __name__, template_folder="../templates")

UPLOAD_FOLDER = "uploads"

@bp.route("", methods=["GET", "POST"])
def vocab():
    structured = None
    raw = None
    message = None
    if request.method == "POST":
        image = request.files.get("image")
        typed = request.form.get("description", "")
        transcription = typed.strip()
        image_desc = "(no image)"
        image_path = None

        if image and image.filename:
            image_path = os.path.join(UPLOAD_FOLDER, image.filename)
            image.save(image_path)
            image_desc = "(attached image)"

        prompt = build_vocab_prompt(image_desc=image_desc, transcription=transcription or typed)
        raw = call_gemma_cli(prompt, image_path=image_path)
        try:
            structured = json.loads(raw.strip().split("\n")[-1])
        except Exception:
            structured = {"error": raw}
        log_vocab_attempt(typed, transcription, structured)
    return render_template("vocab.html", structured=structured, raw=raw, message=message)
