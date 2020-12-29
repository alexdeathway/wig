import sys
from colorama import init, Fore, Style

argument={
        "--proxy ":"Tunnel through a proxy (format: localhost:8080) leave blank for None",


        }

def WigSuccess(message):
    sys.exit(Fore.LIGHTGREEN_EX + message + Style.RESET_ALL)

def WigExit(message):
    sys.exit( Fore.LIGHTRED_EX + message + Style.RESET_ALL)

def getresponse():
    positive=["Yes","yes","y","Y"]
    print("Looks like you are facing problem with CLI.")
    reponse=str(input("\n Enter wizard mode (yes/no)."))
    if reponse in positive:
        return 1
    return 0

def wizard():
    command="python3 wig.py "+str(input("\n Enter Target url:"))

    return command


