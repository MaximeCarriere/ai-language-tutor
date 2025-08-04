import os
import json
import base64
import re
from flask import Blueprint, render_template, request, jsonify, current_app
from services.ollama import call_gemma_cli
from prompts import build_letter_drawing_prompt

bp = Blueprint("letter_drawing", __name__, template_folder="../templates")

# Ensure the upload folder exists
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@bp.route("", methods=["GET", "POST"])
def drawing_practice():
    if request.method == "POST":
        data = request.get_json()
        image_data_url = data.get("image_data")
        target_letter = data.get("letter", "A").upper()

        try:
            header, encoded = image_data_url.split(",", 1)
            image_bytes = base64.b64decode(encoded)
            image_path = os.path.join(UPLOAD_FOLDER, "drawing.png")
            with open(image_path, "wb") as f:
                f.write(image_bytes)

            # --- DEBUGGING PRINT STATEMENT ---
            # This will confirm in your terminal that the image was saved.
            current_app.logger.info(f"Image saved to '{image_path}'. Sending to Gemma for analysis.")

            # Ask the AI to identify the letter without any hints.
            prompt = build_letter_drawing_prompt()
            raw_feedback = call_gemma_cli(prompt, image_path=image_path)

            # This is a more robust way to find the JSON block
            try:
                json_start = raw_feedback.find('{')
                json_end = raw_feedback.rfind('}') + 1
                if json_start != -1 and json_end > json_start:
                    json_str = raw_feedback[json_start:json_end]
                    structured_feedback = json.loads(json_str)
                    
                    # Check for correctness here, in Python
                    recognized_letter = structured_feedback.get("recognized_letter", "").upper()
                    structured_feedback['is_correct'] = (recognized_letter == target_letter)
                else:
                    raise ValueError("No JSON object found in the AI response.")

            except (json.JSONDecodeError, ValueError) as e:
                current_app.logger.error(f"Failed to parse Gemma's JSON. Error: {e}. Raw: {raw_feedback}")
                structured_feedback = {
                    "recognized_letter": "N/A",
                    "feedback": "Sorry, I had trouble understanding the feedback.",
                    "is_correct": False
                }

            return jsonify(structured_feedback)

        except Exception as e:
            current_app.logger.error(f"Error processing drawing: {e}")
            return jsonify({"error": "An error occurred on the server."}), 500

    return render_template("letter_drawing.html")
