import requests
import json
from Body.Listen import Listen
from Body.Speak import Speak

def latestnews():
    api_dict = {"business": "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=c15f55eaa8814b23b5d2f7f209906f09",
                "entertainment": "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=c15f55eaa8814b23b5d2f7f209906f09",
                "health": "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=c15f55eaa8814b23b5d2f7f209906f09",
                "science": "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=c15f55eaa8814b23b5d2f7f209906f09",
                "sports": "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=c15f55eaa8814b23b5d2f7f209906f09",
                "technology": "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=c15f55eaa8814b23b5d2f7f209906f09"
                }

    content = None
    url = None
    Speak("Which field news do you want, [business] , [health] , [technology], [sports] , [entertainment] , [science]")
    field = Listen().lower()
    print(field)
    for key, value in api_dict.items():
        if key.lower() in field:
            url = value
            print(url)
            print("url was found")
            break
        else:
            url = True
    if url is True:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    Speak("Here is the first news.")

    arts = news["articles"]
    for articles in arts:
        article = articles["title"]
        print(article)
        Speak(article)
        news_url = articles["url"]
        print(f"for more info visit: {news_url}")

        Speak("Do you want to hear more news please speak yes or no")
        a = Listen().lower()
        if a == "yes":
            pass
        elif a == "no":
            break

    Speak("thats all")