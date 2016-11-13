from flask import render_template
from app import app
from flask import request
import json
import trip_api


@app.route('/')
@app.route('/index.html', methods = ['GET', 'POST'])
def index():
    return render_template("index.html",
                           title='Home')
@app.route('/search.html')
def search():
    value = request.url[40:]
    vals = value.split('+')
    key = ""
    for item in vals:
        key += item + ' '
    print key

    trip_api.main(key)
    return render_template("search.html")
