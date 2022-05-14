from flask import Flask, render_template, request, render_template

app = Flask(__name__)


@app.route("/")  # home page
def index():
    return render_template("index.html")
