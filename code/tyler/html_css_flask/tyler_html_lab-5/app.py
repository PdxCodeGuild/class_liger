from flask import Flask, render_template

app = Flask(__name__)


@app.route('/') # home page
def index():
    return render_template('index.html')

# export FLASK_APP=app.py && export FLASK_ENV=development