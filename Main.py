from types import coroutine
import pyttsx3
import speech_recognition as sr
from Features import GoogleSearch
from win10toast import ToastNotifier
from keyboard import press_and_release,press
from pyautogui import click
from keyboard import press
from keyboard import press_and_release
from keyboard import write
from time import sleep
import webbrowser as web

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

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

        r.pause_threshold = 0.5

        audio = r.listen(source)
        


    try:

        print(": Recognizing...")

        query = r.recognize_google(audio,language='en-in')

        print(f": Your Command : {query}\n")

    except:
        return ""

    return query.lower()


def TaskExe():

    while True:

        query = TakeCommand()

        if 'google search' in query:
            GoogleSearch(query)
        
        elif 'youtube search' in query:
            Query = query.replace("jarvis","")
            query = Query.replace("youtube search","")
            from Features import YouTubeSearch
            YouTubeSearch(query)

        elif 'set alarm' in query:
            from Features import Alarm
            Alarm(query)

        elif 'download' in query:
            from Features import DownloadYouTube
            DownloadYouTube()
            
        elif 'speed test' in query:
            from Features import SpeedTest
            SpeedTest()

        elif 'whatsapp message' in query:

            name = query.replace("whatsapp message","")
            name = name.replace("send ","")
            name = name.replace("to ","")
            Name = str(name)
            Speak(f"Whats The Message For {Name}")
            MSG = TakeCommand()
            from Automations import WhatsappMsg
            WhatsappMsg(Name,MSG)

        elif 'call' in query:
            from Automations import WhatsappCall
            name = query.replace("call ","")
            name = name.replace("jarvis ","")
            Name = str(name)
            WhatsappCall(Name)

        elif 'show chat' in query:
            Speak("With Whom ?")
            name = TakeCommand()
            from Automations import WhatsappChat
            WhatsappChat(name)

#CHROME AUTOMATIONS

        elif 'chrome' in query:
            from Automations import ChromeAuto
            
            ChromeAuto(query)
            
        elif 'new tab' in query:

            press_and_release('ctrl + t')

        elif 'close tab' in query:

            press_and_release('ctrl + w')

        elif 'new window' in query:

            press_and_release('ctrl + n')

        elif 'history' in query:

            press_and_release('ctrl + h')

        elif 'download' in query:

            press_and_release('ctrl + j')

        elif 'bookmark' in query:

            press_and_release('ctrl + d')

            press('enter')

        elif 'incognito' in query:

            press_and_release('Ctrl + Shift + n')

        elif 'switch tab' in query:
            
            Speak("To which tab Sir?")
            
            tab = TakeCommand()
            
            Tab = int(tab)
            
        
#YOUTUBE AUTOMATIONS
        
        elif 'youtube' in query:
            
            from Automations import YouTubeAuto
            YouTubeAuto(TakeCommand)
        
        elif 'pause' in query:

            press('space bar')

        elif 'resume' in query:

            press('space bar')

        elif 'full screen' in query:

            press('f')

        elif 'film screen' in query:

            press('t')

        elif 'skip' in query:

            press('l')

        elif 'back' in query:

            press('j')

        elif 'increase' in query:

            press_and_release('SHIFT + .')

        elif 'decrease' in query:

            press_and_release('SHIFT + ,')

        elif 'previous' in query:

            press_and_release('SHIFT + p')

        elif 'next' in query:

            press_and_release('SHIFT + n')
        
        elif 'search' in query:

            click(x=916, y=670)

            Speak("What To Search Sir ?")

            search = TakeCommand()

            write(search)

            sleep(0.8)

            press('enter')

        elif 'mute' in query:

            press('m')

        elif 'unmute' in query:

            press('m')

        elif 'my channel' in query:

            web.open("https://www.youtube.com/channel/UCZ0o4tVCnslG3Soke6oGlfQ")
 
 
 #Space Automation Nasa File
           
        elif 'space news' in query:


            Speak("Tell Me The Date For News Extracting Process .")

            Date = TakeCommand()

            from Features import DateConverter

            Value = DateConverter(Date)

            from Nasa import NasaNews

            NasaNews(Value)

        elif 'about' in query:
            from Nasa import Summary
            query = query.replace("jarvis ","")
            query = query.replace("about ","")
            Summary(query)

        elif 'mars images' in query:

            from Nasa import MarsImage

            MarsImage()

#INTERNATIONAL SPACE STATION TRACKER
               
        elif 'track iss' in query:

            from Nasa import IssTracker

            IssTracker()

#ASTEROIDS
        elif ' near earth' in query:
            from Nasa import Astro
            from Features import DateConverter
            Speak("Tell Me The Starting Date .")
            start = TakeCommand()
            start_date = DateConverter(TakeCommand)
            Speak("And Tell Me The End Date .")
            end = TakeCommand()
            end_date = DateConverter(end)
            Astro(start_date,end_date=end_date)
            
# MY LOCATION TRACKER

        elif 'my location' in query:

            from Features import My_Location

            My_Location()

        elif 'where is' in query:

            from Automations import GoogleMaps
            Place = query.replace("where is ","")
            Place = Place.replace("jarvis" , "")
            GoogleMaps(Place)

        elif 'online class' in query:

            from Automations import OnlinClass

            Speak("Tell Me The Name Of The Class .")

            Class = TakeCommand()

            OnlinClass(Class)

        elif 'write a note' in query:

            from Automations import Notepad

            Notepad()

        elif 'dismiss' in query:

            from Automations import CloseNotepad

            CloseNotepad()

        elif 'time table' in query:

            from Automations import TimeTable

            TimeTable()

        elif 'activate the bulb' in query:

            from DataBase.HomeAuto.SmartBulb import Activate

            Activate()

            Speak("Should I Start Or Close The Bulb ?")

            step = TakeCommand()

            if 'close' in step:

                from DataBase.HomeAuto.SmartBulb import CloseLight

                CloseLight()

            elif 'start' in step:

                from DataBase.HomeAuto.SmartBulb import StartLight

                StartLight()

        elif 'corona cases' in query:

            from Features import CoronaVirus

            Speak("Which Country's Information ?")

            cccc = TakeCommand()

            CoronaVirus(cccc)

        else:

            from DataBase.ChatBot.ChatBot import ChatterBot

            reply = ChatterBot(query)

            Speak(reply)

            if 'bye' in query:

                break

            elif 'exit' in query:

                break

            elif 'go' in query:

                break

TaskExe()
