import requests

import json

BASE_URL = "https://icanhazdadjoke.com"

response = requests.get(BASE_URL, headers={'Accept': 'application/json'})

data = json.loads(response.text)

print(data['joke'])

# print(data.keys())