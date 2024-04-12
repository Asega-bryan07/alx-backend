#!/usr/bin/env python3
'''
Use the _ or gettext function to parametrize your
templates. Use the message IDs home_title and home_header.
Create a babel.cfg file containing
'''


from flask import Flask, render_template, request
from flask_babel import Babel


class config(object):
    '''
    configure available languages in our app
    '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# configure the flask app
app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    '''
    Use request.accept_languages to determine the
    best match with our supported languages.
    '''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    '''
    an index.html template
    '''
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
