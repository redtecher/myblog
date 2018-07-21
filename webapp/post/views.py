from . import post
from webapp.models import Post,db,User,Comment
from flask import render_template
from .forms import PostForm,CommentForm
from flask import redirect,url_for
from flask_login import current_user
from datetime import datetime


@post.route('/article/<int:post_id>',methods = ['GET','POST'])  #or  '/article/<int:post_id>'
def article(post_id):
    post = Post.query.filter_by(id = post_id).first()
    form = CommentForm()
    if form.validate_on_submit():
        newcomment = Comment()
        newcomment.name =current_user.name
        newcomment.text =form.content.data
        newcomment.post_id = post.id
        newcomment.user_id = current_user.id
        newcomment.date = datetime.now()
        db.session.add(newcomment)
        db.session.commit()
        return redirect(url_for('.article',post_id = post.id))
        
    comments = Comment.query.filter_by(post_id=post_id).order_by(Comment.date).all()
    
    
    if post is None:
        return redirect(url_for('.listarticle'))
    else:
        title =post.title 
        text =post.text
        publish_date=post.publish_date
        user_id = post.user_id
        user = User.query.filter_by(id = user_id).first()

        return render_template('post.html',form=form,comments=comments,text = text,username = user.username,publish_date = publish_date,siteheading = title,backgroundpic ='/static/img/post2_bg.jpg',post=post)


@post.route('/article',methods = ['GET','POST'])
def listarticle():
    getallpost = Post.query.order_by(Post.publish_date.desc()).all()
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


@post.route('/article/<int:post_id>/comment',methods = ['GET','POST'])
def commentarticle(post_id):
    form = CommentForm()
    post = Post.query.filter_by(id = post_id).first()
    if form.validate_on_submit():
        newcomment = Comment()
        newcomment.name =current_user.name
        newcomment.text =form.content.data
        newcomment.post_id = post.id
        newcomment.user_id = current_user.id
        newcomment.date = datetime.now()
        db.session.add(newcomment)
        db.session.commit()
        return redirect(url_for('.commentarticle',post_id = post.id))
        
    comments = Comment.query.filter_by(post_id=post_id).order_by(Comment.date).all()
    time = datetime.now()
    
    return render_template('post/commentarticle.html',time=time,form=form,post=post,comments=comments,backgroundpic = '/static/img/post-bg.jpg')




@post.route('/article/<int:post_id>/edit',methods=['GET','POST'])
def editarticle(post_id):
    post1 = Post.query.filter_by(id = post_id).first()
    form = PostForm()
    if current_user == post1.user:
        if form.validate_on_submit():
            Post.query.filter_by(id = post_id).update({
                'text':form.text.data,
                'subtitle':form.subtitle.data,
                'title':form.title.data
            })
            
            db.session.commit()
            return redirect(url_for('main.index'))
        form.text.data = post1.text
        form.title.data = post1.title
        form.subtitle.data = post1.subtitle
        return render_template('post/editarticle.html',form=form,backgroundpic = '/static/img/post-bg.jpg')
    else :
        return redirect(url_for('main.index'))

@post.route('/editormd',methods = ['GET','POST'])
def editormd():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(text = form.text.data,title =form.title.data,subtitle = form.subtitle.data,user = current_user._get_current_object(),publish_date = datetime.now())
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('post/editormd.html',form=form,backgroundpic = '/static/img/post-bg.jpg')
    
            
    


