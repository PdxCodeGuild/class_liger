import requests
import json
from secrets import FAVQS_API_KEY

# qotd_url = "https://favqs.com/api/qotd"
search_url = "https://favqs.com/api/quotes?page=3&filter=computer"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Token token={FAVQS_API_KEY}"
}

# include the headers in the request in order to authorize the request on favqs server
response = requests.get(search_url, headers=headers)

data = response.json()

# print(json.dumps(data, indent=2))

# print(json.dumps(data, indent=4))


quotes = data['quotes']

for quote in quotes:
    print(f"{quote['body']}\n\n\t-{quote['author']}\n")