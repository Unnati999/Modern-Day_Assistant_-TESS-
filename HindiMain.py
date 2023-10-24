import pyttsx3
import speech_recognition as sr
from Features import GoogleSearch

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
print(voices)
engine.setProperty('rate',180)

def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

def TakeCommand():
    
    

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print(": Listening....")

        r.pause_threshold = 1

        audio = r.listen(source)
        
    
    try:

        print(": Recognizing...")

        query = r.recognize_google(audio,language='hi')

        print(f": Your Command : {query}\n")

    except:
        return ""

    return query.lower()


TakeCommand()
print(TakeCommand)
def TaskExe():
    while True:
        
        queryHindi = TakeCommand()
        
        if ' हेलो जार्विस' in queryHindi:
            Speak('नमस्ते सर आप कैसे हो')
            
        elif ' कैसे हो ' in queryHindi:
            Speak('मैं ठीक हूँ ')