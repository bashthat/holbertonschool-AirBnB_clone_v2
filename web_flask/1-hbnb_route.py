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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

