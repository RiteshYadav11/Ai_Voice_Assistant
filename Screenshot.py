import pyautogui
import os
from Body.Listen import Listen
from Body.Speak import Speak

def screenshot(Query):
    Query = str(Query).lower()
    if "screenshot" in Query:
        Speak("What should I name the screenshot?")
        filename = Listen().lower()
        folder_path = "C:\\Users\\RITESH YADAV\\Desktop\\AI Voice Assistant\\Screenshot"  # replace with your desired folder path
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        filepath = os.path.join(folder_path, filename + ".png")
        pyautogui.screenshot(filepath)
        Speak("Screenshot saved as " + filename)

    else:
        return False