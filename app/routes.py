from flask_login.utils import logout_user
from app import db, app_obj
import app
from app.models import User, Class, FlashCard, Cardlist
from app.forms import LoginForm, SignInForm, createFlashCardForm, uploadNotes, ClassCreator, fTextInFileForm, ListCreator, FlashCardForm
from flask import render_template, escape, flash, redirect, session
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.utils import secure_filename
import markdown
import os

@app_obj.route('/')
def home():
    form = createFlashCardForm()
       
        
    return render_template('home.html', form=form)

@app_obj.route('/deleteaccount', methods=['GET', 'POST'])
@login_required
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
            is_active = False
            return redirect('/login')
        login_user(user, remember  = form.remember_me.data)
        is_active = True
    return render_template("login.html", title = title, form = form)

@app_obj.route('/find', methods = ['GET', 'POST'])
def find(): 
    title = 'Find Flashcard'
    form = fTextInFileForm()
    if form.validate_on_submit(): 
        flash(f'Loading flashcards with {form.text.data}')
        flashcard = FlashCard.query.filter(FlashCard.content.contains(form.text.data))
        return render_template("flashcards.html", title = title, flashcards = flashcard, form = form)
    return render_template("find.html", title = title, form = form)

@app_obj.route('/createflashcard/<int:list_id>', methods = ['GET', 'POST'])
def create(list_id):
    title = "Create Flashcard"
    form = createFlashCardForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.text.data
        if title is None:
                flash('The FlashCard needs a title')
        elif content is None:
            flash('The content has no text')
        else:
            flashcard = FlashCard(title=form.title.data, content=form.text.data, cardList_id=list_id)
            db.session.add(flashcard)
            db.session.commit()
            flash(f'Flashcard Created: {flashcard}')
    return render_template("createflashcard.html", title = title, form = form)

@app_obj.route('/viewflashcard', methods = ['GET', 'POST'])
@login_required
def view(): 
    title = "View Flashcards"
    flashcards = FlashCard.query.all()
    return render_template("viewflashcards.html", title = title, flashcards = flashcards)
                
@app_obj.route('/uploadnotes/<int:class_id>', methods = ['GET', 'POST'])
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

@app_obj.route("/ClassList", methods = ['GET', 'POST'])
@login_required
def class_selector():
    user_classes = Class.query.filter_by(user_id=current_user.id)
    form = ClassCreator()
    if form.validate_on_submit():
        category = Class(title=form.title.data, user_id=current_user.id)
        db.session.add(category)
        db.session.commit()
        return redirect('/ClassList')
    return render_template('classes.html', 
                           form=form, 
                           user_classes=user_classes)


@app_obj.route("/ClassContent/<int:class_id>", methods = ['GET', 'POST'])
@login_required
def inside_class(class_id):
    class_cardlists = Cardlist.query.filter_by(class_id=class_id)
    form = ListCreator()
    if form.validate_on_submit():
        cardlist = Cardlist(title=form.title.data, class_id=class_id)
        db.session.add(cardlist)
        db.session.commit()
        flash('List {form.data.title} added to this class')
        return redirect(f'/ClassContent/{class_id}')
    class_notes = Cardlist.query.filter_by(class_id=class_id)
    return render_template('inside_class.html',
                    class_id = class_id, 
                    form=form, 
                    cardlists=class_cardlists,
                    notes=class_notes)

@app_obj.route("/flashList/<int:list_id>", methods = ['Get', 'Post'])
@login_required
def flashlist(list_id):
    flashcards = []
    flashcards.extend(FlashCard.query.filter_by(cardList_id=list_id))
    form = FlashCardForm()
    
    if form.validate_on_submit:
        if form.next.data:
            if session['active_card'] == len(flashcards) - 1:
                session['active_card'] = 0
                flash('going to the beginning of the list')
            else:
                session['active_card'] += 1
        elif form.previous.data:
            if session['active_card'] == 0:
                session['active_card'] = len(flashcards) - 1
                flash('going to the end of the list')
            else:
                session['active_card'] -= 1
    
    if len(flashcards) == 0:
            return render_template('flashcard.html', form=form, list_id=list_id)
    return render_template('flashcard.html', form=form, card=flashcards[session['active_card']], list_id=list_id)          
    
