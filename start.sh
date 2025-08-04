#!/usr/bin/env bash
set -e

# 1. Preload the model so it's cached
echo "Pulling Gemma 3n model into Ollama cache..."
ollama pull gemma3

# 2. Start Ollama in background if not running (safe even if already running via brew service)
if ! nc -z 127.0.0.1 11434; then
  echo "Starting Ollama server..."
  ollama serve &>/dev/null &
  sleep 1
fi

# 3. Give Ollama a moment to warm up
echo "Waiting for Ollama to be healthy..."
for i in {1..15}; do
  if ollama run gemma3 --format json <<< "ping" >/dev/null 2>&1; then
    echo "Ollama is ready."
    break
  fi
  sleep 1
done

# 4. Launch the Flask app
echo "Starting Flask app..."
python app.py
