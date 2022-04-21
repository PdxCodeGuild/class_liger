from flask import Flask, render_template, request
import requests


app = Flask(__name__)


@app.route('/') # home page
def index():

    headers = {
        'accept': 'application/json'
    }

    url = "https://icanhazdadjoke.com/"

    response = requests.get(url, headers=headers)

    data = response.json()

    joke_text = data.get('joke')

    # include the joke in the context
    context = {
        'joke_text': joke_text
    }

    return render_template('index.html', context=context)


# TEST_JOKES = [
#     {
#         'joke': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptas, perspiciatis.'
#     }, 
#     {
#         'joke': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptas, perspiciatis.'
#     },
#     {
#         'joke': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptas, perspiciatis.'
#     }
# ]

@app.route('/search', methods=['GET', 'POST'])
def search():

    # pull the search query from the form
    # if the query is empty, set it to a blank string
    search_query = request.form.get('search-query') or ''

    # if using checkboxes, flask/django have .getlist() instead of 
    # .get for accessing multiple values with the same name

    # make the HTTP request
    url = "https://icanhazdadjoke.com/search"

    headers = {
        'accept': 'application/json'
    }

    params = {
        'term': search_query
    }

    response = requests.get(url, headers=headers, params=params)
    data=response.json()


    # Data to render in the template
    context = {
        'jokes': data.get('results'),
        'joke_count': data.get('total_jokes'),
        'search_query': search_query
    }

    return render_template('search.html', context=context)