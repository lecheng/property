import datetime
import json
import os
import uuid
import time

from flask import Flask, jsonify, url_for, Blueprint, redirect, flash
from flask import make_response, request, current_app, render_template, \
    send_from_directory
from flask_login import login_user, logout_user, \
    login_required, current_user
from werkzeug.utils import secure_filename

from playhouse.shortcuts import model_to_dict

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
    email = request.args.get('login_email')
    password = request.args.get('login_password')
    agent = Agent.query.filter_by(agent_email=email).first()
    if agent and bcrypt.check_password_hash(
        agent.password, password):
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

# Register
@agent_blueprint.route('/register',methods=['POST'])
# @crossdomain(origin='*')
def register():
    form = RegisterForm(request.form)
    email = request.args.get('r_email')
    # email = form.email.data
    query = Agent.query.filter_by(agent_email=email).first()
    # return jsonify({"status":form.validate_on_submit()})
    if  query:
        flash("Email exists!",'danger')
    else:
        agent_id = uuid.uuid4()
        agent_name = request.form.get('r_name')
        password = request.form.get('r_password')
        password_confrim = request.form.get('r_password_confirm')
        if password != password_confrim:
            flash("Please confirm your password correctly!","danger")
            return render_template('login.html')
        agent = Agent(
            agent_name=agent_name,
            agent_email=email,
            password=password,
            id=agent_id,
            confirmed=False
        )
        db.session.add(agent)
        db.session.commit()
        token = generate_confirmation_token(agent.agent_email)
        confirm_url = url_for('agent.confirm_email', token=token, _external=True)
        html = render_template('activate.html', confirm_url=confirm_url)
        subject = "Please confirm your email"
        send_email(agent.agent_email, subject, html)

        login_user(agent)
        return redirect(url_for('agent.unconfirmed'))
    return render_template('login.html')

# Confirm
@agent_blueprint.route('/confirm/<token>',methods=['POST','GET'])
@login_required
# @crossdomain(origin='*')
def confirm_email(token):
    if current_user.confirmed:
        flash("Account already confirmed. Please login.","success")
        return redirect(url_for('main.home'))
    email = confirm_token(token)
    agent = Agent.query.filter_by(agent_email=current_user.agent_email).first()
    if agent.agent_email == email:
        agent.confirmed = True
        agent.confirmed_on = datetime.datetime.now()
        mkdir(QRCODE_UPLOAD_FOLDER+agent.agent_email)
        mkdir(QRCODE_UPLOAD_FOLDER+agent.agent_email+'/property')
        db.session.add(agent)
        db.session.commit()
        flash("You have confirmed your account. Thanks!","success")
    else:
        flash("The confirmation link is invalid or has expired.","danger")
    return redirect(url_for('main.home'))

@agent_blueprint.route('/unconfirmed')
@login_required
def unconfirmed():
    if current_user.confirmed:
        return redirect(url_for('main.home'))
    flash('Please confirm your account!', 'warning')
    return render_template('unconfirmed.html')

@agent_blueprint.route('/resend')
@login_required
def resend_confirmation():
    token = generate_confirmation_token(current_user.email)
    confirm_url = url_for('agent.confirm_email', token=token, _external=True)
    html = render_template('activate.html', confirm_url=confirm_url)
    subject = "Please confirm your email"
    send_email(current_user.email, subject, html)
    flash('A new confirmation email has been sent.', 'success')
    return redirect(url_for('agent.unconfirmed'))

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@agent_blueprint.route('/agent/save', methods=["POST"])
@login_required
def agent_save():
    agent = Agent.query.filter_by(agent_email=current_user.agent_email).first()
    agent.agent_email = request.form.get('email')
    agent.agent_license = request.form.get('agent_license')
    agent.agent_phone = request.form.get('us_phone')
    agent.agent_phone_china = request.form.get('chinese_phone')
    agent.agent_wechat = request.form.get('wechat')
    agent.agent_office = request.form.get('address')
    agent.agent_name = request.form.get('name')
    db.session.add(agent)
    db.session.commit()
    return redirect(url_for('main.agent_page'))

@agent_blueprint.route('/upload/', methods=['POST'])
@login_required
def upload():
    agent = Agent.query.filter_by(agent_email=current_user.agent_email).first()
    file = request.files['qrcode']
    filename = secure_filename(file.filename)
    fileurl = 'assets/img/' + agent.agent_email + '/' + filename
    path = os.path.join(*[QRCODE_UPLOAD_FOLDER,agent.agent_email,filename])
    agent.agent_qrcode = fileurl
    folder_path = QRCODE_UPLOAD_FOLDER+agent.agent_email
    filelist = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    # print QRCODE_UPLOAD_FOLDER+agent.agent_email
    # print os.listdir(QRCODE_UPLOAD_FOLDER+agent.agent_email+"/")
    # print filelist

    # remove existing files
    for f in filelist:
        os.remove(os.path.join(folder_path, f))
    file.save(path)
    db.session.add(agent)
    db.session.commit()
    return redirect(url_for('main.agent_page'))
# @agent_blueprint.route('/uploads/<filename>')
# @login_required
# def uploads_file(filename):
#     return send_from_directory(QRCODE_UPLOAD_FOLDER,filename)