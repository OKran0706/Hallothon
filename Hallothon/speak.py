import pyttsx3

def speak_text(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()
    