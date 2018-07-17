#coding:utf-8
from flask_wtf import Form,RecaptchaField
from wtforms import StringField,TextAreaField,PasswordField,BooleanField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,EqualTo,URL,Required,Email,Regexp
from wtforms import ValidationError
from ..models import User,db

class LoginForm(Form):
    email = StringField('电子邮箱',validators=[Required(),Length(1,64),Email()])
    password = PasswordField('密码',[DataRequired()])
    remember_me = BooleanField('记住我')
    submit = SubmitField('登录')



class RegisterForm(Form):
    username =StringField('用户名',validators=[DataRequired(),Length(max=255),Regexp('^[A-Za-z][A-Za-z0-9_.]*$',0,'usernames must be only letters,numbers,dots or underscores')])
    email = StringField('电子邮件',validators=[Email(),Required(),Length(1,64)])
    name = StringField('昵称',validators=[DataRequired(),Length(max = 128)])
    password = PasswordField('密码',validators=[DataRequired(),Length(min=8),EqualTo('password2',message='Passwords must match')])
    password2  =PasswordField('确认密码',validators=[Required()])
    
    #recaptcha =  RecaptchaField()
    submit = SubmitField('注册')

    def validate_email(self,field):
        if User.query.filter_by(email = field.data).first():
            raise ValidationError('Email already registered')
    
    def validate_username(self,field):
        if User.query.filter_by(username = field.data).first():
            raise ValidationError('Username already registered')

    

    '''
    def validate(self):
        check_validate=super(RegisterForm,self).validate()
        if not check_validate:
            return False

        user = User.query.filter_by(username = self.username.data).first()    


        if user:
            self.username.errors.append('User with that name already exits')    

            return False

        return True
    ''' 