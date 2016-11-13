from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
@app.route('/search')
def index():
    user = {'nickname': 'Miguel'}
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        }
    ]

    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)

def search():
    return render_template("search.html")
