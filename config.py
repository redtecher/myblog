import os

class Config(object):
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT= 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = '121674005@qq.com' #os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = 'ewbvioovcwspcaaa' #os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = '121674005@qq.com'
    UPLOAD_FOLDER = os.getcwd()+'/webapp/static/headimg/'
    SAVEPIC = 'webapp/static/savepic/'
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