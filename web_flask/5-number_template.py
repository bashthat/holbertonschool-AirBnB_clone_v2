#!/usr/bin/python3


"""
https://www.youtube.com/watch?v=Aa-F6zqLmig
the set-up for flask
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def message():
    """ returns the desired message """

    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def message_2():
    """/hbnb: displays "HBNB"""

    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def space_case():
    """ display C and the Value"""

    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python(<text>)', strict_slashes=False)
def py3_text(text='is cool'):
    """ holding true to the space case <text>"""

    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def iffnumber(n):
    """ iff  n == integer >> n is a number"""

    return '{:d} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def html_tags(n):
    """ display a HTML page only if n is an integer  """

    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')

