# IMPORTING NECESSARY MODULES
from Modules import *


# HELLO TEXTS
def helloWish():
    helloTexts = ["HELLO!", "HOLA!, THAT'S HELLO IN SPANISH!", "BONJOUR!, HOW ABOUT A HELLO IN FRENCH?",
                  "NAMASTE!", "NAMASKAAR", "HELLOS ARE TOO FORMAL!", "HELLOS ARE BORING!", "WOKE ME UP TO SAY HELLO?",
                  "HI!", "HELLO SUNSHINE!", "HOWDY, PARTNER", "PEEK-A-BOO!",  "HEY THERE!", "I AM IRONMAN", "YO!", "GREETINGS!",
                  "I CAN SAY HELLO IN CHINESE BUT I DON'T LIKE IT", "SHOULD I SAY HELLO? , NAAH!",
                  "GROW UP DUDE!, HELLO IS FOR KIDS!", "REAL MEN SAY SUP MOTHERFUCKER!", "HEY BABY",
                  "HEY!, HONEY-BUNCH", "HEY , I LIKE YOUR VOICE", "HEY , HOW YOU DOIN?", "HUH",
                  "I DON'T SAY HELLO", "YEAH , HELLO. ANYTHING ELSE?",
                  "IF YOU RUINED MY SLEEP JUST TO SAY HELLO , YOU BETTER CARE FOR YOUR LIFE.",
                  "WHAT IS IT?", "OKAY", "HELLO STUPID", "..."]
    helloText = random.choice(helloTexts)
    speak(helloText)

