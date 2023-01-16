from flask import Blueprint, render_template,redirect,url_for,session
from models import *
from config import db



# defino el blueprint
auth_bp = Blueprint('auth_bp', __name__,
    template_folder='templates')


# register (form, necesita conf. de mail)
@auth_bp.route('/register', methods=['GET','POST'])
def signup():
    return '<h1>Register</h1>'


#
@auth_bp.route('/login', methods=['GET','POST'])
def login():
    return '<h1>Login</h1>'