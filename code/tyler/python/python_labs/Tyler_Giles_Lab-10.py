# Use the Dad Joke API to get a dad joke and display it to the user. 
# You may want to also use time.sleep to add suspense.
# Use the requests library to send an HTTP request to https://icanhazdadjoke.com/ 
# with the accept header as application/json. 
# This will return a dad joke in JSON format. 
# You can then use the .json() method on the response to get a dictionary. 
# Get the joke out of the dictionary and show it to the user.

import requests
import json
url = 'https://icanhazdadjoke.com'
headers = {'Accept' : 'application/json'}
response = requests.get(url, headers = headers)
data = response.json()
print(data['joke'])