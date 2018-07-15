from flask import Blueprint
userinfo  = Blueprint('userinfo',__name__)
from . import views
