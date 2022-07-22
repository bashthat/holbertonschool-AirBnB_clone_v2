#!/usr/bin/python3
"""
import modules and start web_flask app
"""
import os
from models import storage
from models import storage.all(...)
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """app route states_list """
    states = (storage.all(State))
    return render_template('7-states_list.html', states=states)


@ app.teardown_appcontext
def teardown_db(exception):
    """ removing SQLAlchemy """
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
