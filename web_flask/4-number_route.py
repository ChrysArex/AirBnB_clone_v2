#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """display “Hello HBNB!”"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello():
    """display “HBNB”"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cstring(text):
    """display “C ” followed by the value of the text variable"""
    return "C " + escape(text).replace('_', ' ')


@app.route("/python/", defaults={'text': 'is cool'})
@app.route("/python/<text>", strict_slashes=False)
def python_string(text):
    """display “Python ”, followed by the value of the text variable"""
    return "Python " + escape(text).replace('_', ' ')


@app.route("/number/<int:n>", strict_slashes=False)
def display_n(n):
    """display “n is a number” only if n is an integer"""
    return "{} is a number".format(escape(n))


app.run(host='0.0.0.0', port=5000)
