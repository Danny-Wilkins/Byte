from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
@app.route('/search')
def index():
    return render_template("index.html",
                           title='Home')

def search():
    return render_template("search.html")
