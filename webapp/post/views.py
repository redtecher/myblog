from . import post
from webapp.models import Post,db,User
from flask import render_template

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

        return render_template('post.html',text = text,username = user.username,publish_date = publish_date,siteheading = title,backgroundpic ='static/img/post-bg.jpg')


@post.route('/article',methods = ['GET','POST'])
def listarticle():
    getallpost = Post.query.all()
    return render_template('listpost.html',allpost=getallpost,backgroundpic = 'static/img/post-bg.jpg')
        



