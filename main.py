# IMPORTING NECESSARY MODULES
import os
import sys
import random

import pyautogui
import pyttsx3
import datetime
import pywhatkit
import requests
import wikipedia
import webbrowser
import speech_recognition

# TAKING USER'S NAME AS INPUT
# name = input("ENTER YOUR NAME : ")
name = "DHANRAJ"

# SETTING THE VOICE
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 200)


# SPEAK FUNCTION
def speak(text):
    engine.say(text)
    engine.runAndWait()


# GREET ACCORDING TO THE TIME
def greetWish():
    hour = datetime.datetime.now().hour
    if 00 <= hour < 12:
        speak("GOOD MORNING" + name)
    elif 12 <= hour < 18:
        speak("GOOD AFTERNOON" + name)
    else:
        speak("GOOD EVENING" + name)


# SOME EXTRA MESSAGES
def extraMessage():
    extraTexts = ["IT IS A GOOD DAY!", "PLEASE STOP RUINING MY SLEEP !", "AAH SHIT !, HERE WE GO AGAIN !",
                  "YOU WON'T LET ME REST, RIGHT?", "IT IS SUCH A BEAUTIFUL DAY ! ", "IT IS A CHEERFUL DAY !",
                  "SOMETIMES I HATE DOING THIS !", "I AM YOUR ASSISTANT", "I AM BUSY, ANYWAYS...",
                  "BRIGHT AND SUNNY DAYS ARE BETTER FOR A WALK"]
    extraText = random.choice(extraTexts)
    speak(extraText)


# ASSISTING MESSAGES
def assistMessage():
    assistTexts = ['HOW CAN I HELP YOU?', 'HOW CAN I ASSIST YOU?', 'WHAT CAN I DO FOR YOU?',
                   'WHAT WOULD YOU LIKE ME TO DO?', 'IS THERE ANYTHING I CAN DO FOR YOU?',
                   'IS THE ANYTHING YOU WANT ME TO DO?']
    assistText = random.choice(assistTexts)
    speak(assistText)


# LISTEN AND INPUT FUNCTIONS
def listenInput():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("LISTENING ... ")
        speak("LISTENING ... ")
        audio = r.listen(source)

    try:
        print("THINKING ... ")
        speak("THINKING ... ")
        query = r.recognize_google(audio, language='en-US')
        print(f"SEARCHED FOR : {query}\n")

    except Exception as e:
        print("SPEAK AGAIN")
        speak("PLEASE SPEAK AGAIN")
        print(e)
        query = None
    return query


# WRAPPING THE FUNCTIONS INTO MAIN
def main():
    query = listenInput()

    # SEARCHING WIKIPEDIA
    if 'Wikipedia' in query:
        speak("SEARCHING ... ")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=1)
        print(results)
        speak(results)

    # PLAYING MUSIC
    elif 'play music' in query.lower():
        music_directory = "E:\\Music\\"
        music = os.listdir(music_directory)
        os.startfile(os.path.join(music_directory, random.choice(music)))

    # ASKING TIME
    elif 'time' in query.lower():
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"It's {time}")

    # OPENING AND CLOSING APPS THAT I FREQUENTLY USE

    # DISCORD
    if 'open discord' in query.lower():
        discord = "C:\\Users\\ASUS\\AppData\\Local\\Discord\\app-1.0.9005\\Discord.exe"
        os.startfile(discord)
    elif 'close discord' in query.lower():
        os.system("taskkill /f /im Discord.exe")

    # PYCHARM
    if 'open python ide' in query.lower():
        pycharm = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.1\\bin\\pycharm64.exe"
        os.startfile(pycharm)
    elif 'close pycharm' in query.lower():
        os.system("taskkill /f /im pycharm64.exe")

    # INTELL IJ
    if 'open java ide' in query.lower():
        intellij = "C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2021.3.2\\bin\\idea64.exe"
        os.startfile(intellij)
    elif 'close java ide' in query.lower():
        os.system("taskkill /f /im idea64.exe")

    # SPOTIFY
    if 'open spotify' in query.lower():
        spotify = "C:\\Users\\ASUS\\AppData\\Roaming\\Spotify\\Spotify.exe"
        os.startfile(spotify)
    elif 'close spotify' in query.lower():
        os.system("taskkill /f /im Spotify.exe")

    # WHATSAPP
    if 'open whatsapp' in query.lower():
        whatsapp = "C:\\Users\\ASUS\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
        os.startfile(whatsapp)
    elif 'close whatsapp' in query.lower():
        os.system("taskkill /f /im WhatsApp.exe")

    # GOOGLE CHROME
    if 'open chrome' in query.lower():
        chrome = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(chrome)
    elif 'close chrome' in query.lower():
        os.system("taskkill /f /im chrome.exe")

    # BRAVE
    if 'open brave' in query.lower():
        brave = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
        os.startfile(brave)
    elif 'close brave' in query.lower():
        os.system("taskkill /f /im brave.exe")

    # OPENING WEBSITES THAT I FREQUENTLY USE
    if 'on internet' in query.lower():
        speak("WHAT SHOULD I SEARCH ?")
        site = listenInput().lower()
        webbrowser.open(f"www.{site}.com")

    # PLAYING SONGS THROUGH YOUTUBE
    if 'on youtube' in query.lower():
        speak("WHAT SHOULD I PLAY ?")
        ytQuery = listenInput().lower()
        pywhatkit.playonyt(ytQuery)

    # TERMINATION
    if 'go to sleep' in query or 'close yourself' in query.lower():
        sys.exit(0)


# calling the main function
greetWish()
extraMessage()
assistMessage()
while True:
    main()
