#coding:utf-8
from webapp.extensions import bcrypt,db,loginmanager
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app


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
    
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    birthday =db.Column(db.Date())
    posts = db.relationship('Post',backref = 'user',lazy = 'dynamic')
    

    
    
    def __repr__(self):
        return "<User '{}'>".format(self.username)




    def set_password (self,password):
        self.password = bcrypt.generate_password_hash(password)
    
    def check_password(self,password):
        return bcrypt.check_password_hash(self.password,password)

    





class Post(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    publish_date = db.Column(db.DateTime())
    user_id = db.Column(db.Integer(),db.ForeignKey('user.id'))
    comments = db.relationship('Comment',backref = 'post',lazy = 'dynamic')
    tags=db.relationship(
        'Tag',secondary =tags,backref = db.backref('posts',lazy='dynamic')
    )
    def __init__(self,title):
        self.title = title
    
    def __repr__(self):
        return "<Post '{}'>".format(self.title)


class Comment(db.Model):
    id=db.Column(db.Integer(),primary_key = True)
    name = db.Column(db.String(255))
    text = db.Column(db.Text())
    date = db.Column(db.DateTime())
    post_id = db.Column(db.Integer(),db.ForeignKey('post.id'))

    def __repr__(self):
        return "<Comment '{}'>".format(self.text[:15])


class Tag(db.Model):
    id = db.Column(db.Integer(),primary_key=True)
    title = db.Column(db.String(255))
    def __init__(self,title):
        self.title = title
    
    def __repr__(self):
        return "<Tag '{}'>".format(self.title)



