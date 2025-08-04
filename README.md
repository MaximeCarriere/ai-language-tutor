# AI-Powered Language Learning Companion

This web application is a personalized language learning tool designed to help users practice and improve their pronunciation, vocabulary, and understanding of letters and numbers. It uses AI, powered by Google's Gemma model, to provide real-time feedback on spoken and written exercises.

## Features

* **Letter Lessons**: In-depth lessons for each letter of the alphabet, including visual recognition across different fonts and practice with associated sounds (phonemes).
* **Letter Exercises**: Interactive quizzes to test letter recognition and identify words containing a specific letter.
* **Vocabulary Practice**: Users can describe an image, and the AI will provide a detailed description and related vocabulary.
* **Math Exercises**: Solve math problems with the help of AI, which can process both text and image-based questions.
* **Audio Input**: Users can record their voice for pronunciation practice, and the application will transcribe the audio and provide feedback.

## Project Structure

The application is built with Python and the Flask web framework. The project is organized into several key directories:


/
|-- app.py              # Main Flask application entry point
|-- routes/             # Contains Flask blueprints for different sections
|   |-- home.py
|   |-- letter.py
|   |-- letter_lesson.py
|   |-- letter_exercises.py
|   |-- vocab.py
|   |-- describe.py
|   |-- math.py
|-- services/           # Modules for interacting with external services (AI, etc.)
|-- persistence/        # Handles data storage and retrieval
|-- prompts/            # Manages the prompts sent to the AI model
|-- templates/          # HTML templates for the user interface
|-- static/             # CSS, JavaScript, and other static assets
|-- uploads/            # Directory for temporary file uploads (audio, images)
|-- README.md           # This file


## Technical Stack

* **Backend**: Python 3, Flask
* **AI Model**: Google Gemma (via Ollama)
* **Audio Transcription**: Whisper.cpp
* **Frontend**: HTML, CSS, JavaScript

## Setup and Installation

To run this project locally, follow these steps:

1.  **Clone the Repository**:
    ```bash
    git clone <your-repository-url>
    cd <repository-directory>
    ```

2.  **Install Dependencies**: It is recommended to use a virtual environment.
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```
    *(Note: You will need to create a `requirements.txt` file listing all necessary Python packages, such as Flask.)*

3.  **Set Up Ollama and Gemma**:
    * Install [Ollama](https://ollama.com/).
    * Pull the Gemma model:
        ```bash
        ollama pull gemma
        ```

4.  **Run the Application**:
    ```bash
    flask run
    ```
    The application will be available at `http://127.0.0.1:5000`.

## How to Use

* Navigate to the homepage to see the available learning modules.
* Select a letter to begin a lesson or exercise.
* In the "Vocabulary" or "Math" sections, you can type a description or upload an image for the AI to analyze.
* For pronunciation practice, allow the browser to use your microphone and record a short audio clip.

---
