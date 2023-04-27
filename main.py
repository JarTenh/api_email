import os
import requests

from send_email import send_email


api_key = os.getenv("NEWSAPI_KEY")
url = f"https://newsapi.org/v2/everything" \
    f"?q=tesla&from=2023-03-27&sortBy=publishedAt&" \
    f"apiKey={api_key}"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Message for the email
msg = """
NEWS FROM newsapi.org:

"""

# Access the article titles and descriptions
for article in content["articles"]:
    msg += article["title"] + "\n"
    msg += article["description"] + "\n"
    msg += "\n"

send_email(msg)
