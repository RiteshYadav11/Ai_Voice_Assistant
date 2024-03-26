from plyer import notification
from pygame import mixer
import os

def showschedule(Query):
    Query = str(Query).lower()
    if"show schedule" in Query:
        file = open("C:\\Users\\RITESH YADAV\\Desktop\\\AI Voice Assistant\\DataBase\\tasks.txt","r")
        content = file.read()
        file.close()
        mixer.init()
        mixer.music.load("C:\\Users\\RITESH YADAV\\Desktop\\AI Voice Assistant\\DataBase\\Notification.mp3")
        mixer.music.play()
        notification.notify(
            title = "My schedule :-",
            message = content,
            timeout = 15
            )
    elif"show my schedule" in Query:
        file = open("C:\\Users\\RITESH YADAV\\Desktop\\AI Voice Assistant\\DataBase\\tasks.txt","r")
        content = file.read()
        file.close()
        mixer.init()
        mixer.music.load("C:\\Users\\RITESH YADAV\\Desktop\\AI Voice Assistant\\DataBase\\Notification.mp3")
        mixer.music.play()
        notification.notify(
            title = "My schedule :-",
            message = content,
            timeout = 15
            )
        return True

    else:
        return False
