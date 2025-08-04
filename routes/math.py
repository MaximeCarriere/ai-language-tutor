from flask import Blueprint, render_template, request
from services.ollama import call_gemma_cli
from persistence.progress import log_math_attempt
from prompts import build_math_prompt
import os

bp = Blueprint("math", __name__, template_folder="../templates")

UPLOAD_FOLDER = "uploads"

@bp.route("", methods=["GET", "POST"])
def math():
    structured = None
    raw = None
    if request.method == "POST":
        question = request.form.get("question", "")
        image = request.files.get("image")
        image_desc = "(no image)"
        image_path = None
        if image and image.filename:
            image_path = os.path.join(UPLOAD_FOLDER, image.filename)
            image.save(image_path)
            image_desc = "(attached image)"

        prompt = build_math_prompt(image_desc=image_desc, question=question)
        raw = call_gemma_cli(prompt, image_path=image_path)
        try:
            structured = json.loads(raw.strip().split("\n")[-1])
        except Exception:
            structured = {"error": raw}
        log_math_attempt(question, structured)
    return render_template("math.html", structured=structured, raw=raw)
