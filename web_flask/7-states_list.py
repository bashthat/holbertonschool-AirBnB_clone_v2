#!/usr/bin/python3
"""
import modules and start web_flask app
"""

from models import *
from models import storage
from flask import Flask, render_template
import models

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """app route states_list, import storage.all, display html states in <h1> header """
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def halt(exc):
    """ removing SQLAlchemy """
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
