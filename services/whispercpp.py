import subprocess
import os

WHISPER_CPP_BIN = os.path.abspath("whisper.cpp/build/bin/whisper-cli")
WHISPER_MODEL = os.path.abspath("whisper.cpp/models/ggml-tiny.en.bin")

def transcribe(wav_path):
    if not os.path.exists(WHISPER_CPP_BIN) or not os.path.exists(WHISPER_MODEL):
        return ""
    cmd = [WHISPER_CPP_BIN, "-m", WHISPER_MODEL, "-f", wav_path, "--no-timestamps"]
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        out = proc.stdout.strip()
        for line in reversed(out.splitlines()):
            if line.strip():
                return line.strip()
    except Exception as e:
        print(f"[ERROR] whisper.cpp failed: {e}")
    return ""
