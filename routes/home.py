from flask import Blueprint, render_template
from services.ollama import is_ollama_up, gemma_health_check


bp = Blueprint("home", __name__, template_folder="../templates")

@bp.route("/")
def index():
    ollama_up = is_ollama_up()
    gemma_ok = gemma_health_check() if ollama_up else False
    return render_template("index.html", ollama_up=ollama_up, gemma_ok=gemma_ok)
