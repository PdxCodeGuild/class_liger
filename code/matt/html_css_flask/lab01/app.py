from flask import Flask, render_template

app = Flask(__name__)


# @app.route("/")  # home page
# def index():
#     return "Hello World!!!!!"


@app.route("/")  # home page
def index():
    return render_template("index.html")
