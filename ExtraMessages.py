# IMPORTING NECESSARY MODULES
from Modules import *


# SOME EXTRA MESSAGES
def extraMessage():
    extraTexts = ["IT IS A GOOD DAY!", "PLEASE STOP RUINING MY SLEEP !", "AAH SHIT !, HERE WE GO AGAIN !",
                  "YOU WON'T LET ME REST, RIGHT?", "IT IS SUCH A BEAUTIFUL DAY ! ", "IT IS A CHEERFUL DAY !",
                  "SOMETIMES I HATE DOING THIS !", "I AM YOUR ASSISTANT", "I AM BUSY, ANYWAYS...",
                  "BRIGHT AND SUNNY DAYS ARE BETTER FOR A WALK"]
    extraText = random.choice(extraTexts)
    speak(extraText)