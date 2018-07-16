#coding:utf-8
from flask_wtf import Form
from wtforms import ValidationError,StringField,SubmitField,TextField
from wtforms.validators import Required,Length
from flask_pagedown.fields import PageDownField

class CommentForm(Form):
    subject = StringField('主题',validators=[Required(),Length(max=64)])
    content = StringField('内容',validators=[Required(),Length(max=255)])


class PostForm(Form):
    title = TextField('标题')
    subtitle = TextField('小标题')
    text = PageDownField("内容：（使用Markdown的语法）",validators=[Required()])
    submit = SubmitField('提交')

    
    