
import requests

url = "https://icanhazdadjoke.com"
headers = {
    "accept": "application/json"
}

response = requests.get(url = "https://icanhazdadjoke.com", headers= headers)

data = response.json()

result = (data["joke"])
print(result)





