from . import userinfo
from flask import render_template,abort
from webapp.models import User

@userinfo.route('/<username>')
def user(username):
    user = User.query.filter_by(username = username).first()
    if user is None:
        abort(404)
    return render_template('userinfo/userinfo.html',user=user,backgroundpic = '/static/img/userinfo_bg.jpg')



