from tkinter import *
import requests
from bs4 import BeautifulSoup

root = Tk()
root.title("Indian Premier League")

url = "https://www.cricbuzz.com/"

def get_score():
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.text,'html.parser')
        team_1 = soup.find_all(class_ = "cb-hmscg-tm-name")[0].get_text()
        team_2 = soup.find_all(class_ = "cb-hmscg-tm-name")[1].get_text()
        team_1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
        team_2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()

        teams.config(text=f"{team_1}\t\t{team_2}")
        scores.config(text=f"{team_1_score}\t\t{team_2_score}")
    except Exception as e:
        e
    scores.after(1000, get_score)

title = Label(root, text='IPL 2023', font=("Haveltica 30 bold"))
title.grid(row=0, pady=5)

teams = Label(root, text="Team 1 vs Team 2", font=("Haveltica 20 bold"))
teams.grid(row=1, padx=5)

scores = Label(root, font=("Haveltica 20 bold"))
scores.grid(row=2, padx=25)

get_score()
root.mainloop()


