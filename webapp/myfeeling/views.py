from . import myfeeling
from webapp.models import Myfeeling
from flask import render_template,redirect,url_for
from flask import request,Response



@myfeeling.route('/')
def feeling():
    getallfeeling  = Myfeeling.query.order_by(Myfeeling.timestamp.desc()).all()
    return render_template('myfeeling/myfeeling.html') 






