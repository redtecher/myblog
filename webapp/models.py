from webapp.extensions import bcrypt,db,loginmanager
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from datetime import datetime

from markdown import markdown

import bleach


tags = db.Table('post_tags',
    db.Column('post_id',db.Integer,db.ForeignKey('post.id')),
    db.Column('tag_id',db.Integer,db.ForeignKey('tag.id'))
    )



@loginmanager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id)) 


class User(UserMixin,db.Model):
    
    id =db.Column(db.Integer(),primary_key = True)
    email = db.Column(db.String(64),unique = True,index = True)
    location = db.Column(db.String(64))
    about_me = db.Column(db.Text())
    member_since = db.Column(db.DateTime(),default = datetime.utcnow)
    last_seen = db.Column(db.DateTime(),default = datetime.utcnow)
    name = db.Column(db.String(64),unique=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    birthday =db.Column(db.Date())
    posts = db.relationship('Post',backref = 'user',lazy = 'dynamic')
    headimg = db.Column(db.String(128),default = None)
    comments = db.relationship('Comment',backref = 'user',lazy = 'dynamic')
    messagesboard =db.relationship('Messageboard',backref = 'user',lazy = 'dynamic')
    myphotos=db.relationship('Photos',backref='user',lazy='dynamic')
    def __repr__(self):
        return "<User '{}'>".format(self.username)




    def set_password (self,password):
        self.password = bcrypt.generate_password_hash(password)
    
    def check_password(self,password):
        return bcrypt.check_password_hash(self.password,password)

    def ping(self):
        self.last_seen = datetime.utcnow()
        db.session.add(self)
        db.session.commit()


    


    





class Post(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    title = db.Column(db.String(255))
    subtitle = db.Column(db.String(255))
    text = db.Column(db.Text())
    publish_date = db.Column(db.DateTime())
    private = db.Column(db.Boolean())
    user_id = db.Column(db.Integer(),db.ForeignKey('user.id'))
    comments = db.relationship('Comment',backref = 'post',lazy = 'dynamic')
    body_html =db.Column(db.Text())
    tags=db.relationship(
        'Tag',secondary =tags,backref = db.backref('posts',lazy='dynamic')
    )
    '''
    @staticmethod
    def on_changed_body(target,value,oldvalue,intitiator):
        allowed_tag = ['a','abbr','acronym','b','blockquote','code','div','em','i','li','ol','pre','strong','table','thead','tbody','tr','th','ul','h1','h2','h3','h4','h5','h6','p',]
        target.body_html = bleach.linkify(bleach.clean(markdown(value,output_html = 'html'),tags=allowed_tag,strip=True))
    '''
    
    

    #处理body字段变化的函数
    @staticmethod
    def on_changed_post(target,value,oldvalue,initiaor):
        allow_tags=['a','abbr','acronym','b','blockquote','code',
                    'em','i','li','ol','pre','strong','ul',
                    'h1','h2','h3','p','img']
        #转换markdown为html，并清洗html标签
        

        target.body_html=bleach.linkify(bleach.clean(
            markdown(value,output_form='html',extensions = ['extra','codehilite']),
            tags=allow_tags,strip=True,
            attributes={
                '*': ['class'],
                'a': ['href', 'rel'],
                'img': ['src', 'alt'],#支持<img src …>标签和属性
            }
    ))

    def __repr__(self):
        return "<Post '{}'>".format(self.title)


class Comment(db.Model):
    id=db.Column(db.Integer(),primary_key = True)
    name = db.Column(db.String(255))
    text = db.Column(db.Text())
    date = db.Column(db.DateTime())
    post_id = db.Column(db.Integer(),db.ForeignKey('post.id'))
    user_id = db.Column(db.Integer(),db.ForeignKey('user.id'))
    def __repr__(self):
        return "<Comment '{}'>".format(self.text[:15])
    

    
    


class Tag(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    title = db.Column(db.String(255))
    def __init__(self,title):
        self.title = title
    
    def __repr__(self):
        return "<Tag '{}'>".format(self.title)

db.event.listen(Post.text,'set',Post.on_changed_post)


class Messageboard(db.Model):
    id =db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(255))
    text = db.Column(db.Text())
    timestamp = db.Column(db.DateTime())
    user_id = db.Column(db.Integer(),db.ForeignKey('user.id'))
    def __repr__(self):
        return "<Messageboard '{}'>".format(self.text[:15])   


class Myfeeling(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    text =db.Column(db.Text())
    user_id = db.Column(db.Integer(),db.ForeignKey('user.id'))
    timestamp = db.Column(db.DateTime())
    def __repr__(self):
        return "<My feeling '{}'>".format(self.text[:15])   
    


class Photos(db.Model):
    id= db.Column(db.Integer(),primary_key = True)
    user_id = db.Column(db.Integer(),db.ForeignKey('user.id'))
    timestamp =  db.Column(db.DateTime())
    pic_url = db.Column(db.Text())
    description =db.Column(db.Text())
    def __repr__(self):
        return "<My Photos '{}'".format(self.text[:15])
    




