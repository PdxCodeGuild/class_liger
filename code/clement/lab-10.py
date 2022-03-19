
import requests

url = "https://icanhazdadjoke.com"
headers = {
    "accept": "application/json"
}

response = requests.get(url = "https://icanhazdadjoke.com", headers= headers)

data = response.json()

result = (data["joke"])
print(result)



joke_choice = input("Please enter what you want a joke about!")



url_search = "https://icanhazdadjoke.com/search?term={joke_choice}"
