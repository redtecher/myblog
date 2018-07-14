from flask_wtf import Form
from wtforms import ValidationError,StringField
from wtforms.validators import Required,Length

class CommentForm(Form):
    subject = StringField('主题',validators=[Required(),Length(max=64)])
    content = StringField('内容',validators=[Required(),Length(max=255)])



    