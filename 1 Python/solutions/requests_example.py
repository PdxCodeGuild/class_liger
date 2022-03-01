import requests
import json 


page = input('which page do you want to see?')

response = requests.get('https://catfact.ninja/breeds', params={'page': page})


print(response.text)