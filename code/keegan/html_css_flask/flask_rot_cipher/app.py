from flask import Flask, render_template, request
from string import ascii_lowercase as ABCs
app = Flask(__name__)


@app.route('/') # home page
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def show_result():

    # print(request.form) # ImmutableMultiDict([('user-string', 'abcabc'), ('r-factor', '13')])
    # print(request.method) # POST

    user_string = request.form.get('user-string')
    r_factor = int(request.form.get('r-factor'))

    result = ''
    for char in user_string:
        if char.isalpha():
            index = ABCs.index(char)
            # increase the index by r-factor
            adjusted_index = (index + r_factor) % 26

            # get the letter at the new index
            result += ABCs[adjusted_index]


        else:
            result += char
            

        context = {
            'result': result,
            'colors': ['#eb57a3', '#928462', '#128937', '#781823']
        }

    # pass the result data to the template through the context variable
    return render_template('result.html', context=context)