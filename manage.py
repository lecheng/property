# manage.py


import os
import unittest
import coverage
import datetime

from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

COV = coverage.coverage(
        branch=True,
        include='myapp/*',
        omit=['*/__init__.py', '*/config/*']
    )
COV.start()

from myapp import app, db
from myapp.models import Agent

app.config.from_object("myapp.config.ProductionConfig")

migrate = Migrate(app, db)
manager = Manager(app)

# migrations
manager.add_command('db', MigrateCommand)

@manager.command
def cov():
    """Runs the unit tests with coverage."""
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    COV.stop()
    COV.save()
    print('Coverage Summary:')
    COV.report()
    basedir = os.path.abspath(os.path.dirname(__file__))
    covdir = os.path.join(basedir, 'tmp/coverage')
    COV.html_report(directory=covdir)
    print('HTML version: file://%s/index.html' % covdir)
    COV.erase()


@manager.command
def create_db():
    """Creates the db tables."""
    db.create_all(bind=None)


@manager.command
def drop_db():
    """Drops the db tables."""
    db.drop_all(bind=None)


@manager.command
def create_admin():
    """Creates the admin user."""
    db.session.add(Agent(
        id="admin_root",
        agent_email="ad@min.com",
        password="admin",
        is_admin=True,
        confirmed=True,
        confirmed_on=datetime.datetime.now(),
        registered_on=datetime.datetime.now())
    )
    db.session.commit()

manager.add_command('runserver',Server(host='0.0.0.0',port=5050))

if __name__ == '__main__':
    manager.run()
