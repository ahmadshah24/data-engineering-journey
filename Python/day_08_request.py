import requests

r = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(r.text)


with open("response.txt", "w") as f:
    f.write(r.text)

