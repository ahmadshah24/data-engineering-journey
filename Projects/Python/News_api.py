
import requests


# query = "computer"
query = input("Enter a topic to search for news: ")

api_key = "f673deb1dcc24bbcb04781ef9be585ff"

url = f"https://newsapi.org/v2/everything?q={query}&from=2026-05-03&sortBy=publishedAt&apiKey={api_key}"


content = requests.get(url).json()


articles = content.get("articles", [])
for index, article in  enumerate(articles):
    title = article.get("title", "No title")
    description = article.get("description", "No description")
    print(f"{index + 1}. Title: {title}\n   Description: {description}\n")
# print(content)


# print(url)


