#!/usr/bin/env python3
'''
instantiate the Babel object in your app. Store it in a
module-level variable named babel.
In order to configure available languages in our app,
you will create a Config class that has a LANGUAGES
class attribute equal to ["en", "fr"].
Use Config to set Babel’s default locale ("en")
and timezone ("UTC").
Use that class as config for your Flask app.
'''

from flask import Flask, render_template
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
babel = Babel(app)


@app.route('/')
def index():
    '''
    an index.html template that simply outputs “Welcome to
    Holberton” as page title
    '''
    return render_template('1-index.html')


if __name__ == '__main__':
app.run(port="5000", host="0.0.0.0", debug=True)
