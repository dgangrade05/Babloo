# IMPORTING NECESSARY MODULES
from Modules import *


# ASSISTING MESSAGES
def assistMessage():
    assistTexts = ['HOW CAN I HELP YOU?', 'HOW CAN I ASSIST YOU?', 'WHAT CAN I DO FOR YOU?',
                   'WHAT WOULD YOU LIKE ME TO DO?', 'IS THERE ANYTHING I CAN DO FOR YOU?',
                   'IS THE ANYTHING YOU WANT ME TO DO?']
    assistText = random.choice(assistTexts)
    speak(assistText)