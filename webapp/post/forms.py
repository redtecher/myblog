#coding:utf-8
from flask_wtf import Form
from wtforms import ValidationError,StringField,SubmitField,TextField,TextAreaField
from wtforms.validators import Required,Length
from flask_pagedown.fields import PageDownField

class CommentForm(Form):
    
    content = StringField('内容',validators=[Required(),Length(max=255)])
    submit = SubmitField('提交')

class PostForm(Form):
    title = TextField('标题',render_kw={"class": "form-control","placeholder": "标题","aria-describedby":"sizing-addon1"})
    subtitle = TextField('小标题',render_kw={"class": "form-control","placeholder": "子标题","aria-describedby":"sizing-addon1"})
    text = TextAreaField("内容：（使用Markdown的语法）",validators=[Required()])
    submit = SubmitField('提交')




    
    