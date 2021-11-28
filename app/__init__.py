from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app_obj = Flask(__name__)
UPLOAD_FOLDER = os.path.join(basedir,'static/mdFiles')
if not os.path.isdir(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

PDF_FOLDER = os.path.join(basedir,'static/pdfFiles')
if not os.path.isdir(PDF_FOLDER):
    os.makedirs(PDF_FOLDER)

IMAGES_FOLDER = os.path.join(basedir,'static/images')
if not os.path.exists(IMAGES_FOLDER):
    os.makedirs(IMAGES_FOLDER)
    
app_obj.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app_obj.config['PDF_FOLDER'] = PDF_FOLDER
app_obj.config['IMAGES_FOLDER'] = IMAGES_FOLDER

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
