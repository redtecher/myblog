from . import myphotos
from forms import PushPicForm
from webapp.models import Post,db,Photos
from flask import render_template
from flask import redirect,url_for,request
from flask_login import login_required
from datetime import datetime

@myphotos.route('/',methods=['GET','POST'])
def showphotos():
    getallphotos =  Photos.query.order_by(Photos.timestamp.desc())
    return render_template('photos/photos.html',getallphotos=getallphotos,backgroundpic ='/static/img/post2_bg.jpg')



@myphotos.route('/<int:photo_id>',methods=['GET','POST'])
def showsinglephoto(photo_id):
    singlephoto = Photos.query.filter_by(id=photo_id).first()
    return render_template('photos/photos.html',singlephoto=singlephoto,backgroundpic='/static/img/post2_bg.jpg')



@myphotos.route('/upload',methods= ['GET','POST'])
@login_required
def uploadphoto():
    form =PushPicForm()
    if form.validate_on_submit():
        if request.method == 'POST':
            if request.files == ImmutableMultiDict([]):
                
                pass
            else:
                upicture = request.files['picture']
                print(upicture)
                fname = upicture.filename
                
                UPLOAD_PIC_FOLDER = current_app.config['UPLOAD_PIC_FOLDER']
                ALLOWED_EXTENSIONS = ['png','jpg','jpeg','gif']
                flag = '.' in fname and fname.rsplit('.',1)[1] in ALLOWED_EXTENSIONS
                if not flag :
                    flash('文件类型错误')
                    return redirect(url_for('.user',username = current_user.username))
                headimg.save('{}{}_{}'.format(UPLOAD__PIC_FOLDER,current_user.username,fname))
                current_user.headimg = '/static/headimg/{}_{}'.format(current_user.username,fname)
    return render_template('photos/upphoto.html',backgroundpic = '/static/img/post2_bg.jpg')
