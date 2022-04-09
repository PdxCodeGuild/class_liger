
import requests


url = "https://icanhazdadjoke.com"
headers = {
    "accept": "application/json"
}


joke_choice = input("Please enter an animal you want a joke about!\n")

url_search = f"https://icanhazdadjoke.com/search?term={joke_choice}"



response = requests.get(url_search, headers = headers)
print(response.text)
data = response.json()

results = data['results']

for jokes in results:
    print(jokes['joke'])





