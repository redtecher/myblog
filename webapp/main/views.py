from . import main
from flask import render_template
from webapp.models import Post
@main.route('/')
def index():
    getallposts = Post.query.all()
    if len(getallposts)>4:
        getallposts=getallposts[:4]

    return render_template('index.html',backgroundpic='static/img/home-bg.jpg',getallposts = getallposts)


@main.route('/about')
def about():
    return render_template('about.html',backgroundpic = 'static/img/about-bg.jpg')


@main.route('/contact')
def contact():
    return render_template('contact.html',backgroundpic = 'static/img/contact-bg.jpg')
