import os, sys

#APP_HOME = r"/Users/chengle/Documents/intern/property/backendnew"
APP_HOME = r"/var/www/html/backendnew"

activate_this = os.path.join(APP_HOME, 'venv/bin/activate_this.py')
execfile(activate_this, dict(__file__=activate_this))

sys.path.insert(0, APP_HOME)
os.chdir(APP_HOME)

from myapp import app as application