#!/usr/bin/env python3
"""
Define a Flask app that implements Babel
for i18n.
"""
from flask import (
        Flask,
        render_template,
        request,
        g
        )
from flask_babel import Babel
from pytz import timezone
from pytz.exceptions import UnknownTimeZoneError
from datetime import datetime


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
    return (render_template("index.html"))


@babel.localeselector
def get_locale():
    """
    Find the best language match based
    on the user's locale.
    """
    language = request.args.get("locale")

    if (language in app.config["LANGUAGES"]):
        return (language)

    if (g.user and g.user.get("locale") in app.config["LANGUAGES"]):
        return (g.user.get("locale"))

    if (request.headers.get("locale") in app.config["LANGUAGES"]):
        return (request.headers.get("locale"))

    return (request.accept_languages.best_match(app.config["LANGUAGES"]))


users = {
        1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
        2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
        3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
        4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
    }


def get_user():
    """
    Fetch a user with the given id.

    Parameters:
        id : int, optional
        The id for the user to fetch. By
        default, no id is assumed to be
        provided.

    Returns:
        The user object bearing the given
        ID otherwise None.
    """
    id = request.args.get('login_as', None)
    if (id is not None and int(id) in users.keys()):
        return users.get(int(id))

    return (None)


@app.before_request
def before_request():
    """
    Intercept request to determine whether user
    is logged in.
    """
    g.user = get_user()
    current_time = datetime.utcnow()
    localized_time = timezone(get_timezone()).localize(current_time)

    g.current_time = localized_time.strftime("%b %d, %Y %I:%M:%S %p")


@babel.timezoneselector
def get_timezone():
    """
    Fetch time zone for user based on user
    locale preference.
    """
    tz = request.args.get("timezone")

    if (timezone):
        try:
            return (timezone(tz).zone)
        except UnknownTimeZoneError:
            pass

    if (g.user and g.user.get("timezone")):
        try:
            return (timezone(tz).zone)
        except UnknownTimeZoneError:
            pass

    return (app.config["BABEL_DEFAULT_TIMEZONE"])
