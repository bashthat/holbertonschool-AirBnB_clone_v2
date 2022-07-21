#!/usr/bin/python3
"""
https://www.youtube.com/watch?v=Aa-F6zqLmig
the set-up for flask
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def message():
    """ returns the desired message """
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def message_2():
    """/hbnb: displays "HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def space_case(text):
    """ display C and the Value along with replacing the space_case@hand '_' = ' ' """
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def py3_text(text = "is cool"):
    """ holding true to the space case, while declaring the text "is cool" for <text>"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def iffnumber(n):
    """ iff  n == integer >> n is a number"""
    return "{:d} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

