from flask import Blueprint, render_template, request
from services.ollama import call_gemma_cli
from persistence.lessons import load_letter_info
from persistence.progress import log_vocab_attempt
from prompts import build_letter_prompt
import os

bp = Blueprint("letter", __name__, template_folder="../templates")

@bp.route("", methods=["GET", "POST"])
def letter():
    structured = None
    raw = None
    letter = request.form.get("letter", "A").upper()
    attempt = request.form.get("attempt", "").strip()
    sound, example_word = load_letter_info(letter)
    if request.method == "POST":
        prompt = build_letter_prompt(letter, learner_attempt=attempt if attempt else None)
        raw = call_gemma_cli(prompt)
        try:
            structured = json.loads(raw.strip().split("\n")[-1])
        except Exception:
            structured = {"error": raw}
        if "sound" not in structured or not structured.get("sound"):
            structured["sound"] = sound
        if "example_word" not in structured or not structured.get("example_word"):
            structured["example_word"] = example_word
        log_vocab_attempt(f"Letter {letter}", attempt, {**structured, "level": "A"})
    return render_template("letter.html", structured=structured, raw=raw, letter=letter, attempt=attempt)
