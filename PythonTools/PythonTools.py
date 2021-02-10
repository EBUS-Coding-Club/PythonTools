#  _____       _   _              _______          _     
# |  __ \     | | | |            |__   __|        | |    
# | |__) |   _| |_| |__   ___  _ __ | | ___   ___ | |___ 
# |  ___/ | | | __| '_ \ / _ \| '_ \| |/ _ \ / _ \| / __|
# | |   | |_| | |_| | | | (_) | | | | | (_) | (_) | \__ \
# |_|    \__, |\__|_| |_|\___/|_| |_|_|\___/ \___/|_|___/
#         __/ |                                          
#        |___/                                           
#Made by Duplexes


#Imports needed to use this code
import os 
from datetime import datetime

#Massive list of colors to easily use on all console systems
Black = "\u001b[30m"    
Red = "\u001b[31m"
Green = "\u001b[32m"
Yellow = "\u001b[33m"
Blue = "\u001b[34m"
Magenta =  "\u001b[35m"
Cyan = "\u001b[36m"
White = "\u001b[37m"
Reset = "\u001b[0m" # Used in premade messages. Must be included to function correctly.
BrightBlack = "\u001b[30;1m"
BrightRed = "\u001b[31;1m" # Used in premade messages. Must be included to function correctly. 
BrightGreen = "\u001b[32;1m" # Used in premade messages. Must be included to function correctly.
BrightYellow = "\u001b[33;1m"
BrightBlue = "\u001b[34;1m"
BrightMagenta = "\u001b[35;1m"
BrightCyan = "\u001b[36;1m" # Used in premade messages. Must be included to function correctly.
BrightWhite = "\u001b[37;1m"

#Premade message functions 
def successmessage(successmessage):
    print("[" + BrightGreen + "Success" + Reset + "] " + successmessage)
def errormessage(errormessage, logerror):
    print("[" + BrightRed + "Error" + Reset + "] " + errormessage)
    def errorlogger():
        if logerror == "true":
            if os.path.exists("errorlog.txt"):
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                errorlogging = open("errorlog.txt", "a")
                errorlogging.write(current_time + " ERROR: " + errormessage + "\n")
            else: 
                 errorlogging = open("errorlog.txt", "x") 
                 errorlogger()
    errorlogger()

def infomessage(infomessage):
    print("[" + BrightCyan + "Info" + Reset + "] " + infomessage)
# Premade tools and functions / lambdas 
clear = lambda: os.system('cls' if os.name=='nt' else 'clear') # This must be run when the program starts to clear a color bug on windows consoles.
def clearlog(): # Function to clear the log file. 
    if os.path.exists("errorlog.txt"):
        f = open("errorlog.txt", "w")
        f.write("")
        f.close()
    else: 
        errorlogging = open("errorlog.txt", "x") 