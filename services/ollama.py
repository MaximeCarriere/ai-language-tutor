# services/ollama.py
import subprocess
import socket
import time
import json

# Configuration (adjust paths if needed)
OLLAMA_CMD = "/opt/homebrew/bin/ollama"
OLLAMA_HOST = "127.0.0.1"
OLLAMA_PORT = 11434
MODEL_NAME = "gemma3"

def is_ollama_up(timeout=1.0):
    try:
        with socket.create_connection((OLLAMA_HOST, OLLAMA_PORT), timeout=timeout):
            return True
    except Exception:
        return False

def ensure_ollama_running():
    if is_ollama_up():
        return True
    try:
        subprocess.Popen([OLLAMA_CMD, "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except FileNotFoundError:
        print(f"ERROR: Ollama binary not found at {OLLAMA_CMD}.")
        return False
    deadline = time.time() + 15
    while time.time() < deadline:
        if is_ollama_up():
            return True
        time.sleep(0.5)
    print("WARNING: Ollama failed to start.")
    return False

def gemma_health_check():
    try:
        proc = subprocess.run(
            [OLLAMA_CMD, "run", MODEL_NAME, "--format", "json"],
            input="ping",
            capture_output=True,
            text=True,
            timeout=5,
        )
        return proc.returncode == 0 and bool(proc.stdout.strip())
    except Exception:
        return False

def call_gemma_cli(prompt: str, image_path: str | None = None, timeout: int = 25) -> str:
    cmd = [OLLAMA_CMD, "run", MODEL_NAME, "--format", "json"]
    if image_path:
        prompt = prompt + f"\n\n[Image attached at {image_path}]"
    try:
        proc = subprocess.run(
            cmd,
            input=prompt,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
    except Exception as e:
        return json.dumps({"error": f"Ollama invocation failed: {e}"})
    output = proc.stdout.strip()
    if proc.stderr:
        output += f"\n\n[stderr]\n{proc.stderr.strip()}"
    return output
