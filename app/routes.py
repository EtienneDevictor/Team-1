from app import app_obj
from app import db
from app.models import User
from app.forms import LoginForm
from flask import render_template, escape, flash, redirect
from flask_login import current_user, login_user, login_required

@app_obj.route('/signup')
def signup():
	form = LoginForm()
	return render_template("signup.html", form = form)

@app_obj.route('/deleteaccount')
def delete():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data)
		if user is None or not user.check_password(form.password.data):
			flash('Invalid username or password')	
			redirect ('/deleteaccount') 
		db.session.delete(user)
		db.session.commit()
		flash(f'{form.username} has been deleted')
	return render_template("delete.html", form = form)
