#!/usr/bin/env python3
"""
Define a Flask app that implements Babel
for i18n.
"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """ Configuration for Babel. """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route(
        "/",
        strict_slashes=False
        )
def index():
    """
    Handle requests to the root directory.
    """
    return (render_template("0-index.html"))
