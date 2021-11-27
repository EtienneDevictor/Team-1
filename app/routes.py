from flask.helpers import send_from_directory, url_for
from flask.templating import render_template_string
from flask_login.utils import logout_user
from app import db, app_obj
import app
from app.models import *
from app.forms import *
from flask import render_template, escape, flash, redirect, session, request
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.utils import secure_filename
from xhtml2pdf import pisa
import markdown
import os

@app_obj.route('/')
def home():
    form = createFlashCardForm()       
    app = 'Study App'    
    return render_template('home.html', form=form, app=app)

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
            return redirect('/')
        login_user(user, remember  = form.remember_me.data)
        is_active = True
        flash('Successfully logged in')
    return render_template("login.html", title = title, form = form)

@app_obj.route('/find', methods = ['GET', 'POST'])
@login_required
def find(): 
    title = 'Find Flashcard'
    form = fTextInFileForm()
    if form.validate_on_submit(): 
        flash(f'Loading flashcards with {form.text.data}')
        user_classes = current_user.classes
        flashlists = []
        for category in user_classes:
            flashlists.extend(Cardlist.query.filter_by(class_id=category.id))
        flashcards = []
        for flashlist in flashlists:
            flashcards.extend(FlashCard.query.filter(FlashCard.content.contains(form.text.data), FlashCard.cardList_id==flashlist.id))
        
        return render_template("viewflashcards.html", title = title, flashcards = flashcards)
    return render_template("find.html", title = title, form = form)

@app_obj.route('/createflashcard/<int:list_id>', methods = ['GET', 'POST'])
@login_required
def create(list_id):
    title = "Create Flashcard"
    form = createFlashCardForm()
    if form.validate_on_submit():
        if form.create.data:
            title = form.title.data
            content = form.text.data
            image = form.image.data
            if title is None:
                flash('The FlashCard needs a title')
            elif content is None:
                flash('The content has no text')
            else:
                if image is not None:
                    image.save(os.path.join(app_obj.config['IMAGES_FOLDER'], title+'.jpg'))
                flashcard = FlashCard(title=title, content=content, cardList_id=list_id)
                db.session.add(flashcard)
                db.session.commit()
                form.title.data = ""
                form.text.data = ""
                flash(f'Flashcard Created: {flashcard.title}')
        elif form.back.data:
            return redirect(f'/flashList/{list_id}')
    return render_template("createflashcard.html", title = title, form = form, list_id=list_id)

@app_obj.route('/viewflashcard/<int:list_id>', methods = ['GET', 'POST'])
@login_required
def view(list_id): 
    title = "View Flashcards"
    flashcards = FlashCard.query.filter_by(cardList_id=list_id)
    return render_template("viewflashcards.html", title = title, flashcards = flashcards, list_id=list_id)
                
@app_obj.route('/uploadnotes/<int:class_id>', methods = ['GET', 'POST'])
@login_required
def notes(class_id):
    title = 'Upload Notes'
    form = uploadNotes()
    if form.validate_on_submit():
        name = form.title.data
        file = form.notes.data
        notes = Notes(class_id = class_id, title = name)
        file.save(os.path.join(app_obj.config['UPLOAD_FOLDER'], name))
        db.session.add(notes)
        db.session.commit()
        flash(f'Notes: {name} Saved')
        return redirect('/uploadnotes/' + str(class_id))
    if form.is_submitted():
        flash('Please enter a md file')
    return render_template('uploadnotes.html', title = title, form = form)


@app_obj.route('/viewnotes/<int:class_id>', methods = ['GET', 'POST'])
@login_required
def viewnotes(class_id):
    title = 'Notes'
    names = Notes.query.filter_by(class_id = class_id)
    path = '/app/mdFiles/'
    return render_template('viewnotes.html', title = title, names = names, path = path, class_id = class_id)
    
@app_obj.route('/app/mdFiles/<name>', methods = ['GET', 'POST'])
def opener(name):
    with open('./app/mdFiles/' + name) as f:
        text = f.read()
        html = markdown.markdown(text)
    return render_template_string(html)
    #Have this extend the base html

@app_obj.route('/app/mdFiles/<name>/convert', methods = ['GET', 'POST'])
def converter(name):
    with open('./app/mdFiles/' + name) as f:
        title = 'Converted'
        file_name = f'{name}.pdf'
        text = f.read()
        html = markdown.markdown(text)
        file_path = f'./app/pdfFiles/{name}.pdf'
        output = open(file_path, "w+b")
        pisa_status = pisa.CreatePDF(html, dest = output)
        output.close()
        return render_template('converted.html', title = title, file_name = file_name)

@app_obj.route('/app/pdfFiles/<name>', methods = ['GET', 'POST'])
def download(name):
    return send_from_directory(directory=os.path.join(app_obj.root_path,'pdfFiles'), path=name)
        

@app_obj.route("/logout")
@login_required
def logout():
    logout_user()
    flash('User logged out')
    return redirect('/login')

@app_obj.route("/ClassList", methods = ['GET', 'POST'])
@login_required
def class_selector():
    user_classes = current_user.classes
    form = ClassCreator()
    if form.validate_on_submit():
        category = Class(title=form.title.data)
        db.session.add(category)
        category.users.append(current_user)
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
    session['active_card'] = 0
    session['front'] = True
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
    image = os.path.join(app_obj.config['IMAGES_FOLDER'], 'asd.jpg')
    
    if form.validate_on_submit():
        if form.next.data:
            session['front'] = True
            if session['active_card'] == len(flashcards) - 1:
                session['active_card'] = 0
                flash('going to the beginning of the list')
            else:
                session['active_card'] += 1
        elif form.previous.data:
            session['front'] = True
            if session['active_card'] == 0:
                session['active_card'] = len(flashcards) - 1
                flash('going to the end of the list')
            else:
                session['active_card'] -= 1
        elif form.flip.data:
            if session['front']:
                session['front'] = False
            else:
                session['front'] = True
    
    if len(flashcards) == 0:
        return render_template('flashcard.html', form=form, list_id=list_id)
    return render_template('flashcard.html', form=form, card=flashcards[2], front=False, list_id=list_id, image = image)          
    
@app_obj.route("/quiz/<int:list_id>/<int:question_num>", methods = ['GET', 'POST'])
@login_required
def quiz(list_id,question_num):
    title = 'Quiz'
    form = QuizForm()
    global answersheet
    questions = {}
    flashcards = []
    flashcards.extend(FlashCard.query.filter_by(cardList_id=list_id))
    qLength = len(flashcards)
    for flashcard in flashcards:
        questions[flashcard.title] = flashcard.content
    form = QuizForm()

    if form.is_submitted():
        if request.form['answer']:  
            answer = request.form['answer']
            answersheet[question_num]=answer
        if form.submit.data:
            flash('submitted')
            counter = 0
            for x in range (0,qLength):
                if answersheet[x] == flashcards[x].title:
                    counter += 1
            flash(f'{counter} correct out of {qLength}')
            return redirect(f'/quiz/{list_id}/{question_num}')
        if form.next.data:
            question_num = up(question_num, qLength)
        elif form.previous.data:
            question_num = down(question_num, qLength)
        return redirect(f'/quiz/{list_id}/{question_num}')
    return render_template('quiz.html', list_id=list_id, title=title, form=form, qNum=question_num, questions=questions, flashcards=flashcards, qLength=qLength, answersheet=answersheet)


def up(num, length):
    if num == length:
        return length
    if num > -1:
        return num + 1

def down(num, length):
    if num == 0:
        return 0
    if num < length + 1:
        return num - 1
    
answersheet = {}

@app_obj.route("/ShareClass/<int:class_id>", methods = ['POST', 'GET'])
@login_required
def share_class(class_id):
    form = ShareClassForm()
    
    if form.validate_on_submit:
        user = User.query.filter_by(username=form.username.data).first()
        category = Class.query.filter_by(id=class_id).first()
        if user:
            category.users.append(user)
            db.session.commit()
            flash(f'{category.title} shared with {user.username}')
        else:
            flash(f'{form.username.data} does not exist')
            
    return render_template('shareclass.html', form=form, class_id=class_id)       
    