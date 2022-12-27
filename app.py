from flask import Flask
from flask import request
app = Flask(__name__)
@app.route("/")
def sum_of_get_params():
    print(request)
    return "<p>Hello, World!</p>"
