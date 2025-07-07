# 📁 File: DialectApp/utils/stt.py

import speech_recognition as sr

listener = None
recognized_text = ""

def callback(recognizer, audio):
    global recognized_text
    try:
        recognized_text = recognizer.recognize_google(audio)
    except:
        recognized_text = ""

def start_listening(lang="en-IN"):
    global listener, recognized_text

    try:
        mic = sr.Microphone()
    except Exception:
        raise RuntimeError("Microphone input is not available in this environment.")

    r = sr.Recognizer()
    r.adjust_for_ambient_noise(mic)

    listener = r.listen_in_background(mic, callback, phrase_time_limit=10)
    recognized_text = ""

def stop_listening():
    global listener
    if listener:
        listener(wait_for_stop=False)
        listener = None
    return recognized_text




