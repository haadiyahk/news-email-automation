import os
from dotenv import load_dotenv  

import requests 
from send_news_mail import send_email

load_dotenv()
api_key = os.getenv("NEWSAPI_API_KEY2")  

print("API Key:", api_key)

url = "https://newsapi.org/v2/top-headlines?"\
    "country=us&"\
    "category=entertainment&"\
    f"apiKey={api_key}&"\
    "language=en"

request= requests.get(url)

content= request.json()

print(content)

body = "Subject: Today's News\n\n"

for article in content["articles"][:20]:
    if article["title"] is not None:
        body=body+article["title"] + "\n" + str(article["description"]) + "\n" + article["url"] + 2*"\n"

# print(body)

body = body.encode("utf-8")
send_email(message=body)