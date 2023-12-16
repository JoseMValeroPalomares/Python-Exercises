import pyttsx3
import re
import speech_recognition as sr

def initialize_engine():
    engine = pyttsx3.init()
    engine.setProperty("rate", 120)
    engine.setProperty("voice", "spanish")
    return engine

def recognize_voice(r):
    with sr.Microphone() as source:
        print("Ya hemos detectado tu microfono, habla")
        audio = r.listen(source)
        text = r.recognize_google(audio, language="es-ES")
    return text

def identify_name(text):
    name = None
    patterns = [r"me llamo ([A-Za-z]+)", r"mi nombre es ([A-Za-z]+)", r"^([A-Za-z]+)$"]
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            name = match.group(1)
            break
    if not name:
        print("No me has dicho tu nombre")
    return name

def main():
    engine = initialize_engine()
    engine.say("Hola como te llamas")
    engine.runAndWait()

    r = sr.Recognizer()
    text = recognize_voice(r)
    name = identify_name(text)
    if name:
        engine.say("Encantado de conocerte {}".format(name))
    else:
        engine.say("No te he entendido")
    engine.runAndWait()

if __name__ == "__main__":
    main()

