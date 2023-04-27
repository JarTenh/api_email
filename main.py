import requests


api_key = "e596321926764516b47fed89d3b44b47"
url = f"https://newsapi.org/v2/everything" \
    f"?q=tesla&from=2023-03-27&sortBy=publishedAt&" \
    f"apiKey={api_key}"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and descriptions
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
