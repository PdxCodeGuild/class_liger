from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/') # home page
# def index():
#     return """
#         <h1>Hello world!</h1>
#         <div>
#             <p>Class Liger</p>
#         </div>
#     """


@app.route('/') # home page
def index():

    # define some data to pass as the 'context' data for the template
    context = {
        'name': 'Keegan',
        'city': 'Portland'
    }

    return render_template('index.html', context=context)