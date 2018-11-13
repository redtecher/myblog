from . import myphotos
from webapp.models import Post,db,Photos
from flask import render_template
from flask import redirect,url_for
from datetime import datetime

@myphotos.route('/',methods=['GET','POST'])
def myphotos():
    getallphotos =  Photos.query.order_by(Photos.timestamp.desc())
    return render_template('photos/photos.html',getallphotos=getallphotos,backgroundpic ='/static/img/post2_bg.jpg')

