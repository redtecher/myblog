import os

class Config(object):
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT= 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = os.environ.get('MAIL_USERNAME')
    UPLOAD_FOLDER = os.getcwd()+'/webapp/static/headimg/'
    UPLOAD_PHOTOS_FOLDER=os.getcwd()+'/webapp/static/picture/'
    SAVEPIC = 'webapp/static/savepic/'
    UPLOADED_PHOTOS_DEST =  os.path.join(os.getcwd(),'static/upload/image')
    @staticmethod
    def init_app(app):
        pass


class ProConfig(Config):
    pass




class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@112.74.173.234:3306/myblog"
    SECRET_KEY = 'hard to guess'
    RECAPTCHA_PUBLIC_KEY="6Ld0DGMUAAAAAJD-DhdCOkM2MnkH9HrQoXY_uqvq"
    RECAPTCHA_PRIVATE_KEY ="6Ld0DGMUAAAAAOmr7l-zO6noPUylXOLzTolZzqAo"
