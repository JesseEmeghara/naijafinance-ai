from gtts import gTTS
import os
import tempfile
import platform

def speak(text):
    tts = gTTS(text)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        filename = fp.name
    tts.save(filename)

    if platform.system() == "Windows":
        os.system(f'start {filename}')
    else:
        os.system(f'afplay {filename}' if platform.system() == "Darwin" else f'mpg123 {filename}')
