from flask import Flask,redirect,url_for

from .extensions import bcrypt,db,loginmanager,bootstrap,mail

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_name)
    config_name.init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)
    loginmanager.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    
    
    return app 