#!/usr/bin/env python3
"""A basic Flask app."""
from typing import Dict, Union
from flask import Flask, g, render_template, request
from flask_babel import Babel

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


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """Determines the best match for language."""
    return (
        request.args.get('locale', None) or
        (g.user and g.user.get('locale', None)) or
        request.accept_languages.best_match(app.config["LANGUAGES"]) or
        "en"
    )


@app.route('/')
def home() -> str:
    """Returns a simple template."""
    user_logged_in = False
    username = ''
    if g.user:
        user_logged_in = True
        username = g.user['name']
    return render_template('6-index.html',
                           user_logged_in=user_logged_in,
                           username=username
                           )


def get_user(id: str | None) -> Union[Dict, None]:
    """Returns a user if the id exists else None."""
    try:
        user = users.get(int(id), None)
    except Exception:
        user = None
    return user


@app.before_request
def before_request() -> None:
    """Sets up routes."""
    user_id = request.args.get('login_as', None)
    user = get_user(user_id)
    g.user = user


if __name__ == "__main__":
    app.run()
