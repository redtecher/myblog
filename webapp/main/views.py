from . import main
from flask import render_template

@main.route('/')
def index():
    return render_template('index.html',backgroundpic='static/img/home-bg.jpg')


@main.route('/about')
def about():
    return render_template('about.html',backgroundpic = 'static/img/about-bg.jpg')
