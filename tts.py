# 📁 File: DialectApp/utils/tts.py

from gtts import gTTS
import tempfile

def text_to_speech(text, lang_code='en'):
    """
    Converts text to speech using gTTS and returns a temporary mp3 file path.
    
    Parameters:
    - text (str): The text to convert to speech.
    - lang_code (str): The language code for the TTS engine (default is 'en').

    Returns:
    - str: Path to the temporary mp3 file that can be played using Streamlit's st.audio()
    """
    try:
        tts = gTTS(text=text, lang=lang_code)
        temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        tts.save(temp_audio.name)
        return temp_audio.name
    except Exception as e:
        print(f"[ERROR] TTS failed: {e}")
        return None




