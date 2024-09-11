from win32com.client import Dispatch
import speech_recognition as sr
from model import *

speak = Dispatch("SAPI.SpVoice")
voices = speak.GetVoices()

# List available voices
# for i, voice in enumerate(voices):
#     print(f"Voice {i}: {voice.GetDescription()}")

speak.Voice = voices.Item(2)

def Speech(output):
    speak.Speak(f"{output}")


def SpeechRecognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=1
        print("listening")
        audio = r.listen(source)
    try:
        print("Recognising")
        query = r.recognize_google(audio, language="en-us")
        print(f"User : {query}\n")
    except Exception:
        print("I am Unable to understand")
        return "None"
    return query

while(True):
    text = SpeechRecognition()
    text = text.lower()

    if "exit" in text or "bye" in text:
        exit()
    else:
        response = predict(text)
        Speech(response)
