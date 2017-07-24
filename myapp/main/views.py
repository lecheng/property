# myapp/main/views.py


#################
#### imports ####
#################

from flask import render_template
from flask import Blueprint
from flask_login import current_user
from flask_login import login_required

################
#### config ####
################

main_blueprint = Blueprint('main', __name__,)


################
#### routes ####
################

#Home page
@main_blueprint.route('/home')
@login_required
def home():
    return render_template('home.html', current_user=current_user)

#Login page
@main_blueprint.route('/login_page',methods=['GET'])
def login_page():
    return render_template('login.html')

#Agent page
@main_blueprint.route('/agent',methods=['GET'])
@login_required
def agent_page():
    return render_template('agent.html')

#Agent page
@main_blueprint.route('/example',methods=['GET'])
@login_required
def example_page():
    return render_template('example.html')