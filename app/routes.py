from flask_login.utils import logout_user
from app import db, app_obj
import app
from app.models import User
from app.forms import LoginForm, SignInForm, createFlashCardForm, uploadNotes
from flask import render_template, escape, flash, redirect
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.utils import secure_filename
import markdown
import os

@app_obj.route('/')
def home():
    form = createFlashCardForm()
       
        
    return render_template('home.html', form=form)

@app_obj.route('/deleteaccount', methods=['GET', 'POST'])
def delete():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
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

@app_obj.route('/uploadnotes', methods = ['GET', 'POST'])
#@login_required
def notes():
    title = 'Notes'
    form = uploadNotes()
    if form.validate_on_submit():
        name = form.title.data + '.html'
        md = markdown.Markdown()
        file = md.convert(form.notes.data)
        '''
        I'm having trouble here
        not sure how to use os to save the html output from 
        file into templates folder
        still need to add into data base as well
        '''
        print(os.path.join(app, name))
        redirect('/name')
    else:
        flash('Please enter a markdown file')
        redirect('/uploadnotes')
    return render_template('uploadnotes.html', title = title, form = form)

@app_obj.route("/logout")
@login_required
def logout():
    logout_user()
    flash('User logged out')
    return redirect('/login')
