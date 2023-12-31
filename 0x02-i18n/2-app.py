#!/usr/bin/env python3
"""A basic Flask app."""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """A configuration class for the Flask app."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Determines the best match for language."""
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def home():
    """Returns a simple template."""
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(debug=True)
