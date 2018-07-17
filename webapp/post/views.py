from . import post
from webapp.models import Post,db,User
from flask import render_template
from .forms import PostForm
from flask import redirect,url_for
from flask_login import current_user
from datetime import datetime


@post.route('/article/<int:post_id>',methods = ['GET','POST'])  #or  '/article/<int:post_id>'
def article(post_id):
    post = Post.query.filter_by(id = post_id).first()
    if post is None:
        return None
    else:
        title =post.title 
        text =post.text
        publish_date=post.publish_date
        user_id = post.user_id
        user = User.query.filter_by(id = user_id).first()

        return render_template('post.html',text = text,username = user.username,publish_date = publish_date,siteheading = title,backgroundpic ='/static/img/post2_bg.jpg',post=post)


@post.route('/article',methods = ['GET','POST'])
def listarticle():
    getallpost = Post.query.all()
    return render_template('listpost.html',allpost=getallpost,backgroundpic = '/static/img/post-bg.jpg')



@post.route('/writearticle',methods = ['GET','POST'])
def writearticle():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(text = form.text.data,title =form.title.data,subtitle = form.subtitle.data,user = current_user._get_current_object(),publish_date = datetime.now())
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('post/writearticle.html',form=form,backgroundpic = '/static/img/post-bg.jpg')

        


