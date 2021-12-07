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
import time

@app_obj.route('/')
def home():
    '''
    renders home.html template
	
    returns:
	    rendering of home.html
    '''
    form = createFlashCardForm()       
    app = 'Study App' 
    return render_template('home.html', form=form, app=app)

@app_obj.route('/deleteaccount', methods=['GET', 'POST'])
@login_required
def delete():
    '''
    takes in the login and password of a user and 
    removes Users() from the database

    returns: 
        rendering of delete.html with LoginForm()
    '''
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
    '''
       takes in user entered info to create a Users() object in and 
       enters it into the database
	
    returns: rendering of signup.html with SignInForm() <br> 
    '''
    header = 'Register Account'
    form = SignInForm()
    if form.validate_on_submit():
        username = User.query.filter_by(username=form.username.data).first()
        email = User.query.filter_by(email=form.email.data).first()
        if username is not None:
                flash('The username is already taken')
        elif email is not None:
            flash('The provided username already belongs to another account')
        else:
            flash("Account Created")
            user = User(username=form.username.data, email=form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            return redirect('/login')
    return render_template("signup.html", header=header, title='Sign Up Page', form=form)

@app_obj.route('/login', methods = ['GET', 'POST'])
def login():
    '''
    takes in user entered information to check Users 
    object and matches with database. After verification, logs the user in or denies request

    returns: rendering of login.html with LoginForm()
    '''
    title = 'Login'
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            is_active = False
            return redirect('/login')
        else:
            login_user(user, remember  = form.remember_me.data)
            is_active = True
            flash('Successfully logged in')
            return redirect("/")
    return render_template("login.html", title = title, form = form)

@app_obj.route('/find', methods = ['GET', 'POST'])
@login_required
def find(): 
    '''
    takes in text entered by user and prints all flashcards in the Users() 
    with the text inside their content

    returns:
        rendering of viewflashcards.html with fTextInFileForm() 
    '''
    title = 'Find Flashcard'
    form = fTextInFileForm()
    if form.validate_on_submit(): 
        flash(f'Loading flashcards with {form.text.data}')
        title = f'Find FlashCard ({form.text.data})'
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
    '''
    takes in information from the user to create FlashCard() object that is linked to a provided Cardlist()
	
    parameters:
		    list_id: unique identification number of the list that the flashcard object will be linked to
			
    returns:
		    rendering of createflashcard.html with createFlashCardForm() form attached
    '''
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
    '''
        returns a list view of all the  FlashCard() contained with a provided Cardlist(). 
        Images contained in cards are not displayed in list view
	
        parameters:
		    list_id: unique identification # of the list obj containing specified flashcards
			
        returns:
		    a rendering of viewflashcard.html with a list of flashcards in list with id=list_id
     '''
    title = f"View Flashcards in {Cardlist.query.filter_by(id=list_id).first().title}"
    flashcards = FlashCard.query.filter_by(cardList_id=list_id)
    return render_template("viewflashcards.html", title = title, flashcards = flashcards, list_id=list_id)
                
@app_obj.route('/uploadnotes/<int:class_id>', methods = ['GET', 'POST'])
@login_required
def notes(class_id):
    '''
        takes in user entered information to create a Notes() object and saves it to the database

        parameters:
		    class_id: unique identifacation # of the class object containing specified notes

        returns: renders uploadnotes.html with uploadNotesForm() form 

    '''
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
    return render_template('uploadnotes.html', title = title, form = form, class_id=class_id)


@app_obj.route('/viewnotes/<int:class_id>', methods = ['GET', 'POST'])
@login_required
def viewnotes(class_id):
    '''
         returns a list view of all Notes() in a specified class_id and the ability to use converter(name)
         or upload new uploadNotesForm()

        parameter:
		    class_id: unique identifacation # of the class object containing specified notes

        returns: renders viewnotes.html with a list of notes in specified class_id
    '''
    title = 'Notes'
    names = Notes.query.filter_by(class_id = class_id)
    path = '/app/static/mdFiles/'
    return render_template('viewnotes.html', title = title, names = names, path = path, class_id = class_id)
    
@app_obj.route('/app/static/mdFiles/<name>', methods = ['GET', 'POST'])
def opener(name):
    '''
        takes in the specified Notes() selected and converts the file into a viewable html and displays it

        parameter:
		    name = unique identifier for specified Notes()

        returns: renders base.html and the Notes() attached
    '''
    with open('./app/static/mdFiles/' + name) as f:
        text = f.read()
        html = markdown.markdown(text)
    return render_template('base.html') + render_template_string(html)


@app_obj.route('/app/static/mdFiles/<name>/convert', methods = ['GET', 'POST'])
def converter(name):
    '''
    take in specified [Notes()](/model/#class-notes) selected and converts the file into a html file then create a new file and converts and writes into pdf format.

    parameter: 
	    	name = unique identifier for specified [Notes()](/model/#class-notes)

    returns: renders converted.html with a link to open the converted pdf file
    '''
    with open('./app/static/mdFiles/' + name) as f:
        title = 'Converted'
        file_name = f'{name}.pdf'
        text = f.read()
        html = markdown.markdown(text)
        file_path = f'./app/static/pdfFiles/{name}.pdf'
        output = open(file_path, "w+b")
        pisa_status = pisa.CreatePDF(html, dest = output)
        output.close()
        return render_template('converted.html', title = title, file_name = file_name)

@app_obj.route('/app/static/pdfFiles/<name>', methods = ['GET', 'POST'])
def download(name):
    '''
    displays specified [Notes()](/model/#class-notes) in pdf format 

    parameter:
	    	name = unique identifier for specified [Notes()](/model/#class-notes)

    returns: renders [Notes()](/model/#class-notes) in pdf format
    '''
    return send_from_directory(app_obj.config['PDF_FOLDER'], name)
        
@app_obj.route("/logout")
@login_required
def logout():
    '''
        logs user out then redirects to login page.

        returns: renders login.html 
    '''
    logout_user()
    flash('User logged out')
    return redirect('/login')

@app_obj.route("/ClassList", methods = ['GET', 'POST'])
@login_required
def class_selector():
    '''
        provides a list of the active users classes that they can pick to open or can take in user 
        inputted data to create a new Class() object
	
        returns:
              a rendering of of class.html with a list of classes and the ClassCreator() form
    '''
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
    '''
        provides a list of notes and flashcard lists contained within the class and links 
        to creating new notes and form to create a new Cardlist() object

    parameters:
		class_id: the unique identification number of the Class() object whose Cardlist()  objects are to be listed
		
    returns:
		rendering of inside_class.html with list of flashcards and notes and a ListCreator()

    '''
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

@app_obj.route("/flashList/<int:list_id>/<int:card_id>", methods = ['Get', 'Post'])
@login_required
def flashlist(list_id, card_id):
    '''
        provides a flashcard view of flashcard in specified list with a form to flip 
        and change flashcard; also provides a link to switch to list view(list_id) and to create(list_id) flashcard

    parameters:
		list_id: the unique identification number of the Cardlist() object 
		card_id: the unique identification number of the FlashCard() object to be viewed
		
    returns:
		rendering of flashcards.html with [FlashCardForm()](/forms/#class-flashcardform) and specified flashcard
    '''
    flashcards = []
    flashcards.extend(FlashCard.query.filter_by(cardList_id=list_id))
    form = FlashCardForm()
    title = Cardlist.query.filter_by(id=list_id).first().title
    listLength = len(flashcards)
    global front
    if listLength > 0:
        photo = flashcards[card_id].title+'.jpg'
        image = os.path.join(app_obj.config['IMAGES_FOLDER'], photo)
        has_photo = os.path.exists(image)
    
    if form.is_submitted():
        if form.next.data:
            front = True
            if card_id == listLength - 1:
                card_id = 0
                flash('going to the beginning of the list')
            else:
                card_id += 1
            return redirect(f'/flashList/{list_id}/{card_id}')
        elif form.previous.data:
            front = True
            if card_id == 0:
                card_id = listLength - 1
                flash('going to the end of the list')
            else:
                card_id -= 1
            return redirect(f'/flashList/{list_id}/{card_id}')
        elif form.flip.data:
            if front == True:
                front = False
            else:   
                front = True
            return redirect(f'/flashList/{list_id}/{card_id}')
    if len(flashcards) == 0:
        return render_template('flashcard.html', form=form, list_id=list_id, title=title)
    return render_template('flashcard.html', form=form, listLength=listLength, flashcards=flashcards, card_id=card_id, front=front, list_id=list_id, image = image, photo = photo, has_photo = has_photo, title=title)              

front = True

@app_obj.route("/quiz/<int:list_id>/<int:question_num>", methods = ['GET', 'POST'])
@login_required
def quiz(list_id,question_num):
    '''
    creates the form [QuizForm()](/forms/#class-quizform) and collects the user submitted answers

        parameters:
        list_id: the unique identification number of the Cardlist() object
        question_num: variable to keep track of the question number for the quiz form

        returns: 
        renders quiz.html with the QuizForm()
        when submitted, redirects to show_answers(list_id) and flashes the number of questions answered correctly
    '''
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
            return redirect(f'/quizanswers/{list_id}')
        if form.next.data:
            question_num = up(question_num, qLength)
        elif form.previous.data:
            question_num = down(question_num, qLength)
        return redirect(f'/quiz/{list_id}/{question_num}')
    return render_template('quiz.html', list_id=list_id, title=title, form=form, qNum=question_num, questions=questions, flashcards=flashcards, qLength=qLength, answersheet=answersheet)

def up(num, length):
    '''
        increments the question number by 1 if it is less than the length to move 
        through the QuizForm()

        parameter:
        num: int variable to represent the question number
        length: int variable to represent the total number of quiz questions

        returns:
        if num equals length, returns length, otherwise returns num + 1
    '''
    if num == length:
        return length
    if num > -1:
        return num + 1

def down(num, length):
    '''
    decrements the question number by 1 if it is greater than 0 to move through the QuizForm()

        parameters:
             num: int variable to represent the question number
            length: int variable to represent total number of quiz questions
        returns: 
            if num is equal to 0, returns 0, otherwise returns num - 1
    '''
    if num == 0:
        return 0
    if num < length + 1:
        return num - 1
    
answersheet = {}

@app_obj.route("/ShareClass/<int:class_id>", methods = ['POST', 'GET'])
@login_required
def share_class(class_id):
    '''
        provides a form to that takes user inputted data to give access to another 
        user for a class that they have access to 

        parameters:
		    class_id: the unique identification # of the Class() that is to be shared 
		
        returns: 
		    a rendering of shareclass.html with the ShareClassForm()
    '''
    form = ShareClassForm()
    
    if form.validate_on_submit:
        user = User.query.filter_by(username=form.username.data).first()
        category = Class.query.filter_by(id=class_id).first()
        if user:
            category.users.append(user)
            db.session.commit()
            flash(f'{category.title} shared with {user.username}')
        elif form.username.data is not None:
            flash(f'{form.username.data} does not exist')
            
    return render_template('shareclass.html', form=form, class_id=class_id)       
    

@app_obj.route('/quizanswers/<int:list_id>', methods = ['POST', 'GET'])
@login_required
def show_answers(list_id):
    '''
    generates the questions, user responses, and correct responses to the quiz
    submitted in quiz(list_id,question_num)

        parameters:
        list_id: the unique identification number of the Cardlist() object

        returns:
        rendering of quizanswers.html displaying the quiz questions, user's response to those 
        question, and the correct responses to the questions
    '''
    title = 'Review Quiz'
    global answersheet
    questions = {}
    flashcards = []
    flashcards.extend(FlashCard.query.filter_by(cardList_id=list_id))
    qLength = len(flashcards)
    for flashcard in flashcards:
        questions[flashcard.title] = flashcard.content
    return render_template('quizanswers.html', flashcards=flashcards, qLength=qLength, questions=questions, answersheet=answersheet, title=title, list_id=list_id)

@app_obj.route('/pomodorotimer')
@login_required
def timer():
    title = 'Pomodoro Timer'
    return render_template('pomodoro.html', title = title)

@app_obj.route('/todolisteditor', methods = ['POST', 'GET'])
@login_required
def todo_list() :
    form = ToDoListForm()
    if form.validate_on_submit:
        title = form.title.data
        rank = form.rank.data
        task = Todolist(title=title, rank=rank, user_id = current_user.id)
        db.session.add(task)
        db.session.commit()
        form.title.data = ""
        form.rank.data = ""
    tasks = current_user.todo.order_by(Todolist.rank)
    return render_template('todolist.html', form=form, items=tasks)
    
@app_obj.route('/deleteItem/<int:id>')
@login_required
def delete_item(id):
    toRemove = current_user.todo.filter_by(id=id).first()
    db.session.delete(toRemove)
    db.session.commit()
    return redirect('/todolisteditor')
    
