from app import db, app_obj
from app.models import User
from app.forms import LoginForm
from flask import render_template, escape, flash, redirect
from flask_login import current_user, login_user, login_required

@app_obj.route('/signup')
def signup():
    header = 'Register Account'
    form = LoginForm()
    if form.validate_on_submit():
        flash(str ="attempting to create an account")
        if User.email_exists(form.email.data):
            flash('The provided email already belong to an account')
        elif User.username_exists(form.username.data):
            flash('The provided username already belongs to another account')
        else:
            password_hash = User.generate_password_hash(form.password.data)
            user = User(username=form.username.data,
                        email=form.email.data,
                        password_hash=password_hash)
            db.session.add(user)
            db.session.commit(user)
	return render_template("signup.html", 
                        header=header, 
                       	title='sign up page', 
                        form=form)
