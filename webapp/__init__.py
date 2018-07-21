from flask import Flask,redirect,url_for
import markdown
from .extensions import bcrypt,db,loginmanager,bootstrap,mail,admin,moment,pagedown
from flaskext.markdown import Markdown

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_name)
    config_name.init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)
    loginmanager.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    admin.init_app(app)
    moment.init_app(app)
    pagedown.init_app(app)
    Markdown(app)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/auth')

    from .post import post as post_blueprint
    app.register_blueprint(post_blueprint,url_prefix = '/post')
    
    #from .admin import admin as admin_blueprint
    #app.register_blueprint(admin_blueprint)
    
    from .userinfo import userinfo as userinfo_blueprint
    app.register_blueprint(userinfo_blueprint,url_prefix = '/userinfo')

    return app 