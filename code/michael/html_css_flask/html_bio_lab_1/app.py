from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('bio.html')

# app.run(debug=True)


# put the html file in a folder titled "templates"

# type these commands:

# export FLASK_APP=app.py
# export FLASK_ENV=development
# flask run