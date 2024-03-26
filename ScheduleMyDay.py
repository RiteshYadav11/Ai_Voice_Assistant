# from Body.Listen import Listen
# from Body.Speak import Speak
import speech_recognition as sr
from googletrans import Translator

def Listen():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-hi")

    except:
        return ""
    
    query = str(query).lower()
    return query

def TranslationHinToEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"AI : {data}.")
    return data

def MicExecution():
    query = Listen()
    data = TranslationHinToEng(query)
    return data

import os

def schedule(Query):
    Query = str(Query).lower()
    if "schedule" in Query:
        tasks = []
        # Speak("Do you want to clear old tasks (Plz speak YES or NO)")
        ReturnData = Listen().lower()
        if "yes" in ReturnData:
            file = open("C:\\Users\\RITESH YADAV\\Desktop\\AI Voice Assistant\\DataBase\\tasks.txt","w")
            file.write(f"")
            file.close()
            no_tasks = int(input("Enter the no. of tasks :- "))
            i = 1
            for i in range(no_tasks):
                tasks.append(input("Enter the task :- "))
                file = open("C:\\Users\\RITESH YADAV\\Desktop\\AI Voice Assistant\\DataBase\\tasks.txt","a")
                file.write(f"{i}. {tasks[i]}\n")
                file.close()
        elif "no" in ReturnData:
            i = 2
            no_tasks = int(input("Enter the no. of tasks :- "))
            for i in range(no_tasks):
                tasks.append(input("Enter the task :- "))
                file = open("C:\\Users\\RITESH YADAV\\Desktop\\AI Voice Assistant\\DataBase\\tasks.txt","a")
                file.write(f"{i}. {tasks[i]}\n")
                file.close()


    else:
        return False

schedule("schedule my day")