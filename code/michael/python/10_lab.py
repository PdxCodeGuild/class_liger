#dad joke api

# https://icanhazdadjoke.com/

# Use the Dad Joke API to get a dad joke and display it to the user. You may want to also use time.sleep to add suspense.

# Part 1
# Use the requests library to send an HTTP request to https://icanhazdadjoke.com/ with the accept header as application/json. This will return a dad joke in JSON format. You can then use the .json() method on the response to get a dictionary. Get the joke out of the dictionary and show it to the user.

import requests
import json

# This retrieves the joke by finding the string in the source and then printing a slice containing it

# request = requests.get('https://icanhazdadjoke.com/')
# request_source = request.text
# beg = request_source.find('<p')
# beg += 20
# end = request_source.find('</p>')
# print(request_source[beg:end])

############################################################

request_2 = requests.get('https://icanhazdadjoke.com/', params={'format': 'json'}, headers={'Accept': 'application/json'})
request_json = request_2.json()
print(request_json['joke'])