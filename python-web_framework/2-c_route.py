#!/usr/bin/python3
"""Script that starts a Flask Web 
   application
"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route specifies the root URL '/':display "Hello HBNB!"

    Returns:
    Str:  the string containg the greeting "Hello HBNB!"
    """
    return"Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route specifies the root URL '/':display "hbnb"

    Returns:
    Str:  the string containg the message "HBNB"
    """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def C(text):
    """
    Route specifies the root URL '/c/<text>':display "C with a text"

    Returns:
    Str:  the string containg the message "C + text."
    """
    return "C {}".format(text.replace('_', ''))


if __name__ == '__main__':
    """
    checks if the current script is being run directly
    starts the Flask web application
    """
    app.run(host='0.0.0.0',port=5000)