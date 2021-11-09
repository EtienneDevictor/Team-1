from app import db, app_obj
from app.models import User
from app.forms import LoginForm
from flask import render_template, escape, flash, redirect
from flask_login import current_user, login_user, login_required

@login_required
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

@app_obj.route('/signup', methods=['Get', 'Post'])
def signup():
    header = 'Register Account'
    form = LoginForm()
    if form.validate_on_submit():
        flash("attempting to create an account")
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
            redirect('/')
    return render_template("signup.html", header=header, title='sign up page', form=form)
