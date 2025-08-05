# routes/describe.py

import os
import json
from flask import Blueprint, render_template, request
from werkzeug.utils import secure_filename
from languages import get_lang_config, get_translations
from services.ollama import call_gemma_cli

bp = Blueprint("describe", __name__, template_folder="../templates")

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@bp.route("/", methods=["GET", "POST"])
def describe_practice():
    """Renders an image description page and handles the image submission."""
    lang_code = request.args.get('lang', 'en')
    lang_config = get_lang_config(lang_code)
    translations = get_translations(lang_code)
    
    structured_feedback = None
    raw_feedback = None
    temp_image_path = None

    if request.method == "POST":
        image_file = request.files.get('image')

        # MODIFIED: Simplified logic. We only check for the image now.
        if image_file:
            try:
                filename = secure_filename(image_file.filename)
                temp_image_path = os.path.join(UPLOAD_FOLDER, filename)
                image_file.save(temp_image_path)
                
                # MODIFIED: The prompt is now simpler, asking for a description.
                prompt = f"""
                You are a friendly and fun assistant for a young child.
                Look at the attached image.
                Describe what you see in one short, simple, and happy sentence.
                
                IMPORTANT: Provide your response as a single JSON object with ONLY ONE key called "kids_description".
                
                Example:
                {{"kids_description": "This is a picture of a cute, fluffy puppy taking a nap!"}}
                """
                
                raw_output = call_gemma_cli(prompt=prompt, image_path=temp_image_path)
                
                try:
                    structured_feedback = json.loads(raw_output)
                except json.JSONDecodeError:
                    raw_feedback = f"AI returned invalid JSON:\n\n{raw_output}"

            except Exception as e:
                raw_feedback = f"An unexpected error occurred: {e}"
            finally:
                if temp_image_path and os.path.exists(temp_image_path):
                    os.remove(temp_image_path)
        else:
            # This is the error if no image file was submitted.
            raw_feedback = "Error: You must upload an image to describe."


    return render_template(
        "describe.html",
        lang_config=lang_config,
        lang_code=lang_code,
        t=translations,
        structured=structured_feedback,
        raw=raw_feedback
    )
