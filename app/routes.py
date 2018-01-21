from flask import render_template
from app import app
from app.fireTest import fire

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    print(fire())
    return render_template('index.html', title='Home', user=user, posts=posts, fire=fire())

