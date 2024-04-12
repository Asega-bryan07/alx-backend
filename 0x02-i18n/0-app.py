#!/usr/bin/env python3
'''
setup a basic Flask app in 0-app.py. Create a single / route
and an index.html template that simply outputs “Welcome to
Holberton” as page title (<title>) and “Hello world”
as header (<h1>).
'''

from flask import Flask, render_template


@app.route('/')
def hello_world():
    '''
    an index.html template that simply outputs “Welcome to
    Holberton” as page title
    '''
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
