import os
import requests

from send_email import send_email


api_key = os.getenv("NEWSAPI_KEY")
topic = "ukrainewar"
url = f"https://newsapi.org/v2/everything" \
    f"?q=ukrainewar&" \
    f"language=en&" \
    f"from=2023-03-27&" \
    f"sortBy=publishedAt&" \
    f"apiKey={api_key}"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Message for the email
msg = """Subject: News from newsapi\n
NEWS FROM newsapi.org:

"""

# Access the article titles and descriptions
for article in content["articles"][:20]:
    msg += article["title"] + "\n"
    msg += article["description"] + "\n"
    msg += article["url"] + "\n"
    msg += "\n"

send_email(msg)
