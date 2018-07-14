#coding:utf-8
from flask_wtf import Form,RecaptchaField
from wtforms import StringField,TextAreaField,PasswordField,BooleanField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,EqualTo,URL,Required,Email,Regexp
from wtforms import ValidationError
from ..models import User,db

class LoginForm(Form):
    email = StringField('Email',validators=[Required(),Length(1,64),Email()])
    password = PasswordField('password',[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('LOG IN')



class RegisterForm(Form):
    username =StringField('Username',validators=[DataRequired(),Length(max=255),Regexp('^[A-Za-z][A-Za-z0-9_.]*$',0,'usernames must be only letters,numbers,dots or underscores')])
    email = StringField('Email',validators=[Email(),Required(),Length(1,64)])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=8),EqualTo('password2',message='Passwords must match')])
    password2  =PasswordField('Comfirm Password',validators=[Required()])
    
    #recaptcha =  RecaptchaField()
    submit = SubmitField('Register')

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