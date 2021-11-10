from app import db, app_obj
from app.models import User
from app.forms import LoginForm, SignInForm
from flask import render_template, escape, flash, redirect
from flask_login import current_user, login_user, login_required

@app_obj.route('/')
def home():
    return render_template('home.html')

@app_obj.route('/deleteaccount', methods=['GET', 'POST'])
def delete():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data)
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')	
            return redirect ('/deleteaccount') 
        db.session.delete(user)
        db.session.commit()
        flash(f'{form.username} has been deleted')
    return render_template("delete.html", title = 'Delete Account Page', form = form)

@app_obj.route('/signup', methods=['GET', 'POST'])
def signup():
    header = 'Register Account'
    form = SignInForm()
    if form.validate_on_submit():
        flash("attempting to create an account")
        username = User.query.filter_by(username=form.username.data).first()
        email = User.query.filter_by(email=form.email.data).first()
        if username is not None:
                flash('The username is already taken')
        elif email is not None:
            flash('The provided username already belongs to another account')
        else:
            user = User(username=form.username.data, email=form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            return redirect('/')
    return render_template("signup.html", header=header, title='Sign Up Page', form=form)

@app_obj.route('/login', methods = ['GET', 'POST'])
def login():
    title = 'Login'
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect('/login')
        login_user(user, remember  = form.remember_me.data)
    return render_template("login.html", title = title, form = form)

@app_obj.route("/logout")
@login_required
def logout():
    logout_user()
    flash('User logged out')
    return redirect('/login')
