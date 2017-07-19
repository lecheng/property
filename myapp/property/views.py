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

property_blueprint = Blueprint('property', __name__,)


################
#### routes ####
################

# @main_blueprint.route('/')
# def home():
#     return render_template('home.html', current_user=current_user)
