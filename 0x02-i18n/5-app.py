#!/usr/bin/env python3
"""A basic Flask app."""
from flask import Flask, render_template, request
from flask_babel import Babel, _
import flask

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """A configuration class for the Flask app."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """Determines the best match for language."""
    locale = request.args.get('locale', None)
    if locale:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def home():
    """Returns a simple template."""
    user_logged_in = False
    username = ''
    if flask.g.user:
        user_logged_in = True
        username = flask.g.user['name']
    home_title = _('home_title')
    home_header = _('home_header')
    logged_in_as = _('logged_in_as', username=username)
    not_logged_in = _('not_logged_in')
    return render_template('5-index.html',
                           home_title=home_title,
                           home_header=home_header,
                           user_logged_in=user_logged_in,
                           logged_in_as=logged_in_as,
                           not_logged_in=not_logged_in
                           )


def get_user(id: str):
    """Returns a user if the id exists else None."""
    try:
        user = users.get(int(id), None)
    except Exception:
        user = None
    return user


@app.before_request
def before_request():
    """Sets up routes."""
    user_id = request.args.get('login_as', None)
    user = get_user(user_id)
    flask.g.user = user


if __name__ == "__main__":
    app.run()
