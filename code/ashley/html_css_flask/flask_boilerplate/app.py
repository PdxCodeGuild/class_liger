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

app.run(debug=True)

@app.route('/') # home page
def index():
    return render_template('index.html')