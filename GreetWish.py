# IMPORTING NECESSARY MODULES
from Modules import *

# TAKING USER'S NAME AS INPUT
# name = input("ENTER YOUR NAME : ")
name = "DHANRAJ"


# GREET ACCORDING TO THE TIME
def greetWish():
    hour = datetime.datetime.now().hour
    if 00 <= hour < 12:
        speak("GOOD MORNING" + name)
    elif 12 <= hour < 18:
        speak("GOOD AFTERNOON" + name)
    else:
        speak("GOOD EVENING" + name)