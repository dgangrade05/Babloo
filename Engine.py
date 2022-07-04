# IMPORTING NECESSARY MODULES
from Modules import *

# SETTING THE VOICE
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 200)


# SPEAK FUNCTION
def speak(text):
    engine.say(text)
    engine.runAndWait()

