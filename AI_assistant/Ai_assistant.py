import pyttsx3 as p
import os
import sys
import random
import webbrowser as web
from selenium import webdriver
import speech_recognition as sr
import datetime
from web_Auto import wiki
from news import news
from questions import question
from youtube import video

engine=p.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speck(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    print(hour)
    if hour>=0 and hour<12:
        speck('Good morning')
    elif hour<=12 and hour>18:
        speck("good Afternoon")
    elif hour>=18:
        speck("Good Evening")

    speck("Hi Im AI sir, How mey I help You")

if __name__== "__main__":
    wish()
    while True:
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            r.pause_threshold=1
            audio = r.listen(source)
            print(audio)
        try:
            print("recognizing...")
            query=r.recognize_google(audio,language="en-in")
            print(f"You Said:{query}")
        except Exception as e:
            print(e)
            print("Say That Again....")
            speck("Say That Again....")

        # information for wikipedia
        if "information" in query.lower():
            speck("Information For What")
            r1 = sr.Recognizer()
            with sr.Microphone() as source1:
                print("Listening....")
                r.pause_threshold = 1
                audio1 = r.listen(source1)
                print(audio1)

            try:
                print("recognizing...")
                query = r1.recognize_google(audio1, language="en-in")
                wiki(query)
                print(f"User Said:{query}")
            except Exception as e:
                print(e)
                print("Say That Again....")
                speck("Say That Again....")
            exit()

        # playing music
        elif "play music" in query.lower():
            music="C:\\music"
            songs=os.listdir(music)
            i=random.randint(0,68)
            print(i)
            os.startfile(os.path.join(music,songs[i]))

        elif "open youtube" in query.lower():
            web.open_new("https://www.youtube.com/")

        elif "time" in query.lower():
            time=datetime.datetime.now().strftime("%H:%M")
            speck(f"The time is {time}")

        elif "open code" in query.lower():
            code="C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code)

        elif "open chrome" in query.lower():
            chrome="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            os.startfile(chrome)

        # News
        elif "news" in query.lower():
            speck("Tell Me which category you want to get News")
            r2 = sr.Recognizer()
            with sr.Microphone() as source2:
                print("Listening....")
                r2.pause_threshold = 1
                audio2 = r2.listen(source2)
                print(audio2)

            try:
                print("recognizing...")
                query = r2.recognize_google(audio2, language="en-in")
                news(query)
                print(f"User Said:{query}")
            except Exception as e:
                print(e)
                print("Say That Again....")
                speck("Say That Again....")
            exit()

        # Question and Answers
        elif "I have questions" in query.lower():
            speck("Tell Me what is your question")
            r3 = sr.Recognizer()
            with sr.Microphone() as source3:
                print("Listening....")
                r3.pause_threshold = 1
                audio3 = r3.listen(source3)
                print(audio3)

            try:
                print("recognizing...")
                query = r3.recognize_google(audio3, language="en-in")
                question(query)
                print(f"User Said:{query}")
            except Exception as e:
                print(e)
                print("Say That Again....")
                speck("Say That Again....")
            exit()

        # Play Youtube Videos
        elif "play video" in query.lower():
            speck("Tell Me Video Name")
            r2 = sr.Recognizer()
            with sr.Microphone() as source2:
                print("Listening....")
                r2.pause_threshold = 1
                audio2 = r2.listen(source2)
                print(audio2)

            try:
                # print("recognizing...")
                query = r.recognize_google(audio2, language="en-in")
                video(query)
                print(f"User Said:{query}")
            except Exception as e:
                print(e)
                # print("Say That Again....")
                # speck("Say That Again....")
            exit()

        elif "close" in query.lower():
            sys.exit()



