from flask import Flask
from flask_basicauth import BasicAuth

app = Flask(__name__)

try:
    # development config - values listed in pyfile
    # file excluded from source control
    app.config.from_pyfile('dev_config.py')
except IOError:
    # Production config - values in envvars
    app.config.from_pyfile('config.py')

basic_auth = BasicAuth(app)

from app import views
