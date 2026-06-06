#Trial version of the code to get news from newsapi.org
import os
from dotenv import load_dotenv
import requests

load_dotenv()

api_key = os.getenv("NEWSAPI_API_KEY")
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "sortBy=publishedAt&apiKey=" \
      f"{api_key}"
# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content["articles"]:
    print(article["title"])
    print(article["description"])