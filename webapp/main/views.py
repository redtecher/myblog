from . import main
from flask import render_template,redirect,url_for
from webapp.models import Post,Messageboard,db
from .forms import MessageboardForm
from datetime import datetime
from flask_login import current_user
@main.route('/')
def index():
    getallposts = Post.query.order_by(Post.publish_date.desc()).all()
    if len(getallposts)>4:
        getallposts=getallposts[:4]

    return render_template('index.html',backgroundpic='static/img/home-bg.jpg',getallposts = getallposts)


@main.route('/about')
def about():
    return render_template('about.html',backgroundpic = 'static/img/about-bg.jpg')


@main.route('/contact')
def contact():
    return render_template('contact.html',backgroundpic = 'static/img/contact-bg.jpg')


@main.route('/messageboard',methods=['GET','POST'])
def messageboard():
    form = MessageboardForm()
    if form.validate_on_submit():
        message = Messageboard()
        message.name = current_user.username
        message.text = form.content.data
        message.timestamp = datetime.now()
        message.user_id = current_user.id
        db.session.add(message)
        db.session.commit()
        return redirect(url_for('.messageboard'))

    messages = Messageboard.query.order_by(Messageboard.timestamp.desc()).all()
    return render_template('messageboard.html',siteheading = '留言板',form=form,messages = messages,backgroundpic = 'static/img/contact-bg.jpg')
        
