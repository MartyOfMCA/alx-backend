#!/usr/bin/env python3
"""
Define a basic Flask application.
"""
from flask import (
        Flask,
        render_template
        )


app = Flask(__name__)


@app.route(
        "/",
        strict_slashes=False
        )
def index():
    """
    Handle requests to the root directory.
    """
    return (render_template("0-index.html"))
