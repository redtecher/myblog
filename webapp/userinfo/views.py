#coding:utf-8
from . import userinfo
from flask import render_template,abort,flash,redirect,url_for
from webapp.models import User
from flask_login import login_required,current_user
from .forms import EditMyProfile
from webapp.models import db
from flask import request,current_app

@userinfo.route('/<username>')
def user(username):
    user = User.query.filter_by(username = username).first()
    if user is None:
        abort(404)
    return render_template('userinfo/userinfo.html',user=user,backgroundpic = '/static/img/userinfo_bg.jpg')


@userinfo.route('/editprofile',methods = ['GET','POST'])
@login_required
def edit_profile():
    form =EditMyProfile()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        current_user.birthday = form.birthday.data
        #新增头像功能
        headimg = request.files['headimg']
        fname = headimg.filename
        UPLOAD_FOLDER = current_app.config['UPLOAD_FOLDER']
        ALLOWED_EXTENSIONS = ['png','jpg','jpeg','gif']
        flag = '.' in fname and fname.rsplit('.',1)[1] in ALLOWED_EXTENSIONS
        if not flag :
            flash('文件类型错误')
            return redirect(url_for('.user',username = current_user.username))
        headimg.save('{}{}_{}'.format(UPLOAD_FOLDER,current_user.username,fname))
        current_user.headimg = '/static/headimg/{}_{}'.format(current_user.username,fname)
        



        #end
        db.session.add(current_user)
        db.session.commit()
        flash('Your profile has been updated')
        return redirect(url_for('.user',username = current_user.username))
    headimg = current_user.headimg
    form.name.data=current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    form.birthday.data = current_user.birthday
    return render_template('userinfo/edit_profile.html',form=form,headimg = headimg,backgroundpic = '/static/img/userinfo_bg.jpg')



        