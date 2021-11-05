from app import db
from app.models import User
from myapp.forms import LoginForm
from flask import render_template, escape, flash, redirect
from flask_login import current_user, login_user, login_required

@myobj.route('/signup")
def signup():
	return render_template("signup.html")
