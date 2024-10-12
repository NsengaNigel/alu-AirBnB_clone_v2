#!/usr/bin/python3
"""
Flask web application for AirBnB clone
This module creates a Flask web application that displays a list of all State
objects present in the database. The states are sorted alphabetically by name.
The application listens on 0.0.0.0, port 5000.
"""

from flask import Flask, render_template
from models import storage
from models.state import State
import os


app = Flask(__name__)


@app.teardown_appcontext
def close_db(error):
    """Remove the current SQLAlchemy Session after each request"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Display HTML page with list of all State objects in DBStorage
    States are sorted alphabetically by name
    """
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template('7-states_list.html', states=sorted_states)


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    print(f"Server is running on http://{host}:{port}/")
    print("Press CTRL+C to stop the server")
    app.run(host=host, port=port)
