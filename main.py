from flask import Flask, redirect, url_for, request
from flask.templating import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "homepage"

@app.route('/action')
def action():
    return "action"

if __name__ == '__main__':
   app.run(debug = True,host='0.0.0.0')

