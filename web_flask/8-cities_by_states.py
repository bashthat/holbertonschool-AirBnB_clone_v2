#!/usr/bin/python3
"""
import modules and start web_flask app
"""

from flask import Flask, render_template
from models import storage
from models import *
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=none):
    """app route states_list, import storage.all, display html states in <h1> header """
    states = storage.all("State")
    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def halt(exc):
    """ removing SQLAlchemy """
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
