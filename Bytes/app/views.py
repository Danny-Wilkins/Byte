from flask import render_template
from app import app
import trip_api


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
                           title='Home')
@app.route('/search')
def search():
    return render_template("search.html")
