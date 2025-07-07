import speech_recognition as sr

transcript_buffer = []  # Global buffer to store segments
listener = None         # Listener reference to stop later

def callback(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio)
        transcript_buffer.append(text)
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        transcript_buffer.append(f"[API Error: {e}]")

def start_listening(lang="en-IN"):
    global listener
    r = sr.Recognizer()
    mic = sr.Microphone()
    r.adjust_for_ambient_noise(mic)

    listener = r.listen_in_background(mic, callback, phrase_time_limit=5)
    return "Listening..."

def stop_listening():
    global listener
    if listener:
        listener(wait_for_stop=False)
        listener = None
    full_transcript = " ".join(transcript_buffer)
    transcript_buffer.clear()
    return full_transcript



