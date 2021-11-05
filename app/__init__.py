from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app_obj = Flask(__name__)

app_obj.config.from_mapping(
	SECRET_KEY = 'who cares',
	# location of the app database
	SQLALCHEMY_DATABASE_URE = 'sqlite:///' + 0s.path.join(basedir, 'app.db'),
	SQLACHEMY_TRACK_MODIFICATIONS = False,
)

db = SQLAchemy(app_obj)

login = LoginManager(app_obj)
login.login_view = 'login'
from app import routes, models
