from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_mail import Mail
bcrypt = Bcrypt()
bootstrap = Bootstrap()
db = SQLAlchemy()
loginmanager = LoginManager()
mail = Mail()