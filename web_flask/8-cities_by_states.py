#!/usr/bin/python3
"""
import modules and start web_flask app
"""

from flask import Flask, render_template
imoort models
from models import storage
from models import *

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """app route states_list, import storage.all, display html states in <h1> header """
    states = sorted(list(storage.all("State").values()), key=lambda z: x.name)
    return render_template('8-cities_by_states.html', states=states)

@app.teardown_appcontext
def halt(exc)
    """ removing SQLAlchemy """
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
