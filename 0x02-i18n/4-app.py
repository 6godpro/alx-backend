#!/usr/bin/env python3
"""A basic Flask app."""
from flask import Flask, render_template, request
from flask_babel import Babel


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
    locale = request.args.get('locale', None)
    if locale:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def home():
    """Returns a simple template."""
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run()
