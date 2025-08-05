# routes/story.py

import os
import json
from flask import Blueprint, render_template, request
from werkzeug.utils import secure_filename
from languages import get_lang_config, get_translations, get_story_images
from services.ollama import call_gemma_cli

bp = Blueprint("story", __name__, template_folder="../templates")

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@bp.route("/", methods=["GET", "POST"])
def story_weaver():
    lang_code = request.args.get('lang', 'en')
    lang_config = get_lang_config(lang_code)
    translations = get_translations(lang_code)
    story_images = get_story_images(lang_code)

    story_result = None
    raw_feedback = None
    
    if request.method == "POST":
        temp_files_to_clean = []
        try:
            selected_ids = request.form.getlist('selected_items')
            stock_items_map = {item['id']: item['name'] for item in story_images}
            selected_names = [stock_items_map[id] for id in selected_ids if id in stock_items_map]

            user_images = request.files.getlist('user_images')
            user_image_paths = []
            for image_file in user_images:
                if image_file and image_file.filename:
                    filename = secure_filename(image_file.filename)
                    temp_path = os.path.join(UPLOAD_FOLDER, filename)
                    image_file.save(temp_path)
                    user_image_paths.append(temp_path)
                    temp_files_to_clean.append(temp_path)
            
            if not selected_names and not user_image_paths:
                 raw_feedback = "Please select at least one picture to start your story."
            else:
                prompt_parts = []
                if selected_names:
                    prompt_parts.append(f"The main characters or objects are: {', '.join(selected_names)}.")
                if user_image_paths:
                    prompt_parts.append("Also include things you see in the attached pictures.")

                # --- MODIFIED: The prompt now tells the AI which language to use ---
                prompt = f"""
                You are a magical storyteller for a young child.
                IMPORTANT: You MUST write the story in {lang_config['name']}.

                Create a short, happy, and simple story (2-3 paragraphs).
                {' '.join(prompt_parts)}
                
                Provide your response as a single JSON object with two keys:
                - "title": A fun title for the story (also in {lang_config['name']}).
                - "story_text": The full text of the story (also in {lang_config['name']}).
                """
                # -------------------------------------------------------------------

                raw_output = call_gemma_cli(prompt=prompt, image_path=user_image_paths[0] if user_image_paths else None)
                
                try:
                    story_result = json.loads(raw_output)
                except json.JSONDecodeError:
                    raw_feedback = f"The storyteller got confused and returned this:\n\n{raw_output}"

        except Exception as e:
            raw_feedback = f"An unexpected adventure happened: {e}"
        finally:
            for f_path in temp_files_to_clean:
                if os.path.exists(f_path):
                    os.remove(f_path)

    return render_template(
        "story.html",
        lang_config=lang_config,
        lang_code=lang_code,
        t=translations,
        story_images=story_images,
        story_result=story_result,
        raw_feedback=raw_feedback
    )
