import os

from flask import Flask, render_template, request
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_cors import CORS

################
#### config ####
################

def _check_config_variables_are_set(config):
    assert config['MAIL_USERNAME'] is not None,\
           'MAIL_USERNAME is not set, set the env variable APP_MAIL_USERNAME '\
           'or MAIL_USERNAME in the production config file.'
    assert config['MAIL_PASSWORD'] is not None,\
           'MAIL_PASSWORD is not set, set the env variable APP_MAIL_PASSWORD '\
           'or MAIL_PASSWORD in the production config file.'

    assert config['SECRET_KEY'] is not None,\
           'SECRET_KEY is not set, set it in the production config file.'
    assert config['SECURITY_PASSWORD_SALT'] is not None,\
           'SECURITY_PASSWORD_SALT is not set, '\
           'set it in the production config file.'

    assert config['SQLALCHEMY_DATABASE_URI'] is not None,\
           'SQLALCHEMY_DATABASE_URI is not set, '\
           'set it in the production config file.'

    if os.environ['APP_SETTINGS'] == 'myapp.config.ProductionConfig':
        assert config['STRIPE_SECRET_KEY'] is not None,\
               'STRIPE_SECRET_KEY is not set, '\
               'set it in the production config file.'
        assert config['STRIPE_PUBLISHABLE_KEY'] is not None,\
               'STRIPE_PUBLISHABLE_KEY is not set, '\
               'set it in the production config file.'

app = Flask(__name__)
CORS(app)

app.config.from_object(os.environ['APP_SETTINGS'])

_check_config_variables_are_set(app.config)

####################
#### extensions ####
####################
mail = Mail(app)
login_manager = LoginManager()
login_manager.init_app(app)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

####################
#### blueprints ####
####################

from myapp.main.views import main_blueprint
from myapp.property.views import property_blueprint
from myapp.agent.views import agent_blueprint
app.register_blueprint(main_blueprint)
app.register_blueprint(property_blueprint)
app.register_blueprint(agent_blueprint)

####################
#### flask-login ####
####################
from myapp.models import Agent

login_manager.login_view = "main.login_page"
login_manager.login_message_category = "danger"


@login_manager.user_loader
def load_user(agent_id):
    return Agent.query.filter(Agent.id == agent_id).first()
