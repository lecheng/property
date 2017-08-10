import datetime
import json
import os
import uuid
import time
import md5

from flask import Flask, jsonify, url_for, Blueprint, redirect, flash
from flask import make_response, request, current_app, render_template, \
    send_from_directory
from flask_login import login_user, logout_user, \
    login_required, current_user
from werkzeug.utils import secure_filename

from utils import *
from myapp.models import Agent
from myapp.decorators import *
from myapp.token import generate_confirmation_token, confirm_token
from myapp.email import send_email

from myapp import db, bcrypt
from myapp.agent.forms import RegisterForm

################
#### config ####
################

agent_blueprint = Blueprint('agent', __name__,)
QRCODE_UPLOAD_FOLDER = 'myapp/static/assets/img/'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


#Login
@agent_blueprint.route('/login',methods=['POST','GET'])
# @crossdomain(origin='*')
def login():
    email = request.form.get('login_email')
    password = request.form.get('login_password')
    agent = Agent.query.filter_by(agent_email=email).first()
    m = md5.new()
    m.update(password)
    if agent and m.hexdigest()==agent.password:
        login_user(agent)
        return redirect(url_for('main.home'))
    else:
        flash('Invalid email or password','danger')
        return render_template('login.html')
    return render_template('login.html')

#Logout
@agent_blueprint.route('/logout',methods=['GET'])
@login_required
def logout():
    logout_user()
    flash('You were logged out.','success')
    return redirect(url_for('main.login_page'))