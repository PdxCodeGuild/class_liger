import requests

def version_1():

    url = 'https://icanhazdadjoke.com/'

    response = requests.get(
        url,
        headers={
            'accept': 'application/json'
        },
    )

    data = response.json()

    # check the status of the response, 
    # print an error message if the status code isn't 200
    if data['status'] != 200:
        print(data['message'])
    else:
        joke = data['joke']
        print(joke)

# version_1()

def version_2():
    url = 'https://icanhazdadjoke.com/search'

    response = requests.get(
        url,
        headers={
            'accept': 'application/json'
        },
        params={
            'term': 'computer',
            'page': 1,
            'limit': 5
        }
    )

    data = response.json()

    jokes_list = data['results']

    for joke_data in jokes_list:
        print(joke_data['joke'], end="\n\n")

# version_2()