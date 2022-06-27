# importing necessary modules
import os
import random
import pyttsx3
import datetime
import wikipedia
import speech_recognition

# input user's name
name = input("ENTER YOUR NAME : ")

# setting up the engine and voice
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 200)


# speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()


# greet according to the time function
def greetWish():
    hour = datetime.datetime.now().hour
    if 00 <= hour < 12:
        speak("GOOD MORNING" + name)
    elif 12 <= hour < 18:
        speak("GOOD AFTERNOON" + name)
    else:
        speak("GOOD EVENING" + name)


# assist message function
def assistMessage():
    assistTexts = ['HOW CAN I HELP YOU?', 'HOW CAN I ASSIST YOU?', 'WHAT CAN I DO FOR YOU?',
                   'WHAT WOULD YOU LIKE ME TO DO?', 'IS THERE ANYTHING I CAN DO FOR YOU?',
                   'IS THE ANYTHING YOU WANT ME TO DO?']
    assistText = random.choice(assistTexts)
    speak(assistText)


# listen and input function
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
        query = None
    return query


# calling all the functions
def main():
    speak("INITIALIZING BUBBLOO")

    greetWish()
    assistMessage()
    query = listenInput()

    # searching wikipedia
    if 'Wikipedia' in query:
        speak("SEARCHING ... ")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=1)
        print(results)
        speak(results)

    # playing music
    elif 'play music' in query.lower():
        music_directory = "Music\\"
        music = os.listdir(music_directory)
        os.startfile(os.path.join(music_directory, random.choice(music)))

    # asking the time
    elif 'time' in query.lower():
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"It's {time}")

    # opening apps
    if 'brave' in query.lower():
        brave = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\Brave.exe"
        os.startfile(brave)

    elif 'command' in query.lower():
        cmd = "C:\\WINDOWS\\system32\\cmd.exe"
        os.startfile(cmd)

    elif 'discord' in query.lower():
        discord = "C:\\Users\\ASUS\\AppData\\Local\\Discord\\app-1.0.9005\\Discord.exe"
        os.startfile(discord)

    elif 'chrome' in query.lower():
        chrome = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(chrome)

# calling the main function
main()
