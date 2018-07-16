#coding:utf-8
from flask_wtf import Form
from wtforms import StringField,TextAreaField,SubmitField,DateField,FileField
from wtforms.validators import Required,Length


class EditMyProfile(Form):
    headimg = FileField('头像')
    name = StringField('昵称',validators=[Length(0,64)])
    location = StringField('地点',validators=[Length(0,64)])
    about_me = TextAreaField('个人简介')
    birthday = DateField('生日')
    submit = SubmitField('提交')






