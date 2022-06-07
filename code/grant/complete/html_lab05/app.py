from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/') # home page

def index():

    return render_template('index.html')

# result = ''

# def show():
#     # do code here
#     print(request.form)

#     context = {
#         'result': result,
#     }
#     return render_template('result.html', context=context)
