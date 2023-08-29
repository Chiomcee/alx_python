#!/usr/bin/python3
"""Script that starts a Flask Web 
   application
"""
from flask import Flask, render_template

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
def c_text(text):
    """
    Route specifies the root URL '/c/<text>':display "C with a text"

    Returns:
    Str:  the string containg the message "C + text."
    """
    return "C {}".format(text.replace('_', ' '))

@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """
    Route specifies the root URL "/python/(<text>)". Displays a string.

    Returns:
    str: A string containing the message "Python " + text.
    """
    return "Python " + text.replace("_", " ")

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Route specifies the root URL '/number/<n>'. Display a string
    """
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Route specifies the root URL "/number_template/<n>". Displays a string
    """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    """
    checks if the current script is being run directly
    starts the Flask web application
    """
    app.run(host='0.0.0.0',port=5000)