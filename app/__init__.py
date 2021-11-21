from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app_obj = Flask(__name__)
UPLOAD_FOLDER = basedir + '/mdFiles'
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app_obj.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app_obj.config.from_mapping(
	SECRET_KEY = 'who cares',
	# location of the app database
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
	SQLALCHEMY_TRACK_MODIFICATIONS = False,
)

db = SQLAlchemy(app_obj)

login = LoginManager(app_obj)
login.login_view = 'login'

from app import routes, models
