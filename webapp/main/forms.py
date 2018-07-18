from wtforms import StringField,SubmitField
from flask_wtf import Form
from wtforms.validators import Required,Length


class MessageboardForm(Form):
    content = StringField('内容',validators=[Required(),Length(max=255)])
    submit = SubmitField('提交')