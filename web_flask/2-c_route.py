#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Handles root url"""
    return 'Hello HBNB!'


@app.route('/', strict_slashes=False)
def hbnb():
    """Handles root url"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Handles /c/<text> route"""
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)
