# Pocket Tutor 🚀

**An Offline-First, AI-Powered Literacy Tool for Education in Crisis**

[![Gemma AI Challenge](https://img.shields.io/badge/Made%20for-Gemma%20AI%20for%20Impact%20Challenge-blueviolet)](https://www.kaggle.com/competitions/google-ai-for-impact-challenge)
[![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)](https://www.python.org/)
[![Ollama](https://img.shields.io/badge/Ollama-Local%20AI-lightgrey?logo=ollama)](https://ollama.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Pocket Tutor is an on-device learning application built to function as an educational lifeline in environments where traditional schooling is impossible. It transforms any basic smartphone or laptop into a personal, patient tutor that works entirely without an internet connection, directly addressing the educational crises in regions like Gaza and Afghanistan with dedicated Arabic and Dari language support.

---

## 🎯 Project for the "Gemma AI for Impact Challenge"

This project was conceived and built specifically to meet the core goals of the **Gemma AI for Impact Challenge**: leveraging state-of-the-art AI to create scalable, real-world solutions for humanity's most pressing problems.

Here’s how Pocket Tutor aligns with the spirit of the competition:

**1. Addresses a Critical Humanitarian Need:**
The project directly tackles UN Sustainable Development Goal 4 (Quality Education) for the most vulnerable populations. By creating a tool that functions entirely offline, we provide a resilient solution for the 625,000 children in Gaza without schools and the 80% of school-aged girls in Afghanistan banned from education.

**2. Innovative & Multimodal Use of Gemma:**
Pocket Tutor goes beyond simple text generation. We use Gemma as the core reasoning engine in a complex, on-device multimodal system:
* **Image Understanding (Handwriting Analysis):** Gemma analyzes user-drawn letters to provide instant, encouraging feedback, acting as a virtual handwriting coach.
* **Image-to-Text (Real-World Discovery):** Gemma identifies objects from user-uploaded photos, turning a child's immediate surroundings into an interactive vocabulary lesson.
* **Creative Generation (Storytelling):** Gemma weaves user-selected images into unique, simple stories, providing a source of infinite, personalized reading material in environments where books are scarce.

**3. Technically Ambitious & Privacy-First Architecture:**
The greatest technical challenge was creating a robust, useful application that runs **100% offline**. By using Ollama to serve local instances of Gemma and Whisper, we guarantee:
* **Total Privacy:** No user data (voice, images, progress) ever leaves the device. This is crucial for users in sensitive environments.
* **Zero Latency:** All interactions are instantaneous, creating a seamless user experience.
* **Infinite Scalability:** The solution requires no cloud infrastructure, servers, or data centers. It can be shared peer-to-peer and run on millions of devices at no marginal cost.

**4. Direct Impact & Scalability:**
The application was built with direct impact in mind, offering a full curriculum in Arabic and Dari. The framework is extensible, designed to easily incorporate new languages and content, making it a truly global platform for crisis education.

---

## ✨ Key Features

* **Letter Level:** Interactive lessons with AI-powered handwriting and pronunciation practice.
* **Word Level:** Vocabulary building with structured lessons, matching games, and real-world object recognition.
* **Sentence Level:** Creative expression with speech-to-text and an AI-powered interactive storyteller.
* **Fully Offline:** No internet connection required after initial setup.
* **Completely Private:** All user data is processed and stored locally.
* **Multilingual:** Full support for English, Arabic, and Dari.

---

## 🛠️ Tech Stack

* **Backend:** Python 3.9+ with Flask
* **Local AI Serving:** [Ollama](https://ollama.com/)
* **AI Models:**
    * **Reasoning & Generation:** `gemma:2b`
    * **Image Understanding:** `llava`
    * **Speech-to-Text:** `whisper`
* **Frontend:** HTML, CSS, JavaScript

---

## 💻 Installation and Setup

Follow these instructions to get Pocket Tutor running on your local machine.

### 1. Prerequisites

Make sure you have the following installed on your system:
* [Git](https://git-scm.com/)
* [Python 3.9](https://www.python.org/downloads/) or later
* [Ollama](https://ollama.com/)

### 2. Step-by-Step Guide

**Step 1: Clone the Repository**
Open your terminal and clone this repository to your local machine.
```bash
git clone [https://github.com/](https://github.com/)[your-username]/pocket-tutor.git
cd pocket-tutor
```

**Step 2: Install Python Dependencies**
It's recommended to create a virtual environment first.
```bash
# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install the required packages
pip install -r requirements.txt
```

**Step 3: Download the Required AI Models via Ollama**
This is the most important step. Open your terminal and pull the necessary models. This will download several gigabytes of data, so ensure you have a stable internet connection for this step.

```bash
# Pull the Gemma model for text generation and reasoning
ollama pull gemma:2b

# Pull the Llava model for image understanding (handwriting, object recognition)
ollama pull llava

# Pull the Whisper model for speech-to-text transcription
ollama pull whisper
```
**Note:** You can check that the models are installed correctly by running `ollama list`.

**Step 4: Run the Application**
Once the dependencies are installed and the models are downloaded, start the Flask server.
```bash
python app.py
```

**Step 5: Open Pocket Tutor**
You should see output in your terminal indicating that the server is running. Open your web browser and navigate to:

**[http://127.0.0.1:5000](http://127.0.0.1:5000)**

You can now use Pocket Tutor!

---

## 💡 How It Works

Pocket Tutor operates on a simple yet powerful local AI pipeline:

1.  **User Input:** The user interacts with the frontend, providing input via drawing on a canvas, speaking into the microphone, or uploading an image.
2.  **Flask Backend:** The JavaScript frontend sends this data to the local Flask server.
3.  **Ollama AI Processing:** The Flask app routes the request to the appropriate local model served by Ollama:
    * Drawings and photos go to **Llava** for analysis.
    * Audio files go to **Whisper** for transcription.
    * Text prompts (from Whisper or internal logic) go to **Gemma** for feedback generation or storytelling.
4.  **Response to User:** The AI's response is sent back through Flask to the frontend and displayed to the user instantly.

This entire loop happens on the user's machine, ensuring privacy and offline functionality.

---

## 🗺️ Future Work

* **Adaptive Learning:** Implement a Spaced Repetition System (SRS) to create personalized learning paths.
* **Cross-Platform Accessibility:** Re-platform as a Progressive Web App (PWA) for easy, app-store-free distribution.
* **High-Quality TTS:** Integrate a lightweight, on-device TTS model for more natural-sounding voices.
* **Granular Feedback:** Fine-tune the models to provide more specific, constructive handwriting feedback.
* **Language Expansion:** Add support for more languages spoken in crisis zones.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
