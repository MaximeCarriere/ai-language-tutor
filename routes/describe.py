from flask import Blueprint, render_template, request
from services.ollama import call_gemma_cli
from persistence.progress import log_description_attempt, log_vocab_attempt, log_math_attempt
from prompts import build_description_prompt
import os

bp = Blueprint("describe", __name__, template_folder="../templates")

UPLOAD_FOLDER = "uploads"

@bp.route("", methods=["GET", "POST"])
def describe():
    structured = None
    raw = None
    if request.method == "POST":
        image = request.files.get("image")
        image_desc = "(no image)"
        image_path = None
        if image and image.filename:
            image_path = os.path.join(UPLOAD_FOLDER, image.filename)
            image.save(image_path)
            image_desc = "(attached image)"

        prompt = build_description_prompt(image_desc=image_desc)
        raw = call_gemma_cli(prompt, image_path=image_path)
        try:
            structured = json.loads(raw.strip().split("\n")[-1])
        except Exception:
            structured = {"error": raw}
        log_description_attempt(structured)
    return render_template("vocab.html", structured=structured, raw=raw, mode="describe")
