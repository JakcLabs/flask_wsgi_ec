import os
import sys

activate_this = '/usr/share/flask_wsgi_ec/venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

sys.stdout = sys.stderr

sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '../..'))

sys.path.append('/usr/share/flask_wsgi_ec/')

from flask_wsgi_ec.run import app as application