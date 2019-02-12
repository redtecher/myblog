from . import myphotos
from .forms import PushPicForm
from webapp.models import Post,db,Photos
from flask import render_template,current_app,flash
from flask import redirect,url_for,request
from flask_login import login_required,current_user
from datetime import datetime
from PIL import Image
import os





@myphotos.route('/',methods=['GET','POST'])
def showphotos():
    getallphotos =  Photos.query.order_by(Photos.timestamp.desc())
    return render_template('photos/photos.html',getallphotos=getallphotos,backgroundpic ='/static/img/post2_bg.jpg')



@myphotos.route('/<int:photo_id>',methods=['GET','POST'])
def showsinglephoto(photo_id):
    singlephoto = Photos.query.filter_by(id=photo_id).first()
    username=singlephoto.user.username
    return render_template('photos/photo.html',singlephoto=singlephoto,username=username,backgroundpic='/static/img/post2_bg.jpg')

def random_str(length=32):
    import random
    base_str = 'qwertyuioplkjhgfdsazcxvbnm0123456789'
    return ''.join(random.choice(base_str) for i in range(length))


@myphotos.route('/upload',methods= ['GET','POST'])
@login_required
def uploadphoto():
    form =PushPicForm()
    if form.validate_on_submit():
        photo=Photos()
        photo.timestamp=datetime.now()
        photo.user_id=current_user.id 
        photo.description = form.simpletext.data
        filename = form.photo.data.filename
        UPLOAD_PHOTOS_FOLDER = current_app.config['UPLOAD_PHOTOS_FOLDER']
        form.photo.data.save('{}{}_{}'.format(UPLOAD_PHOTOS_FOLDER,current_user.username,filename))
        photo.pic_url  ='/static/picture/{}_{}'.format(current_user.username,filename)
        db.session.add(photo)
        db.session.commit()
        flash("上传成功","ok")
        return redirect('/myphotos')       
    return render_template('photos/upphoto.html',form=form,backgroundpic='/static/img/post2_bg.jpg')
