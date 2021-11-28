
# Welcome to Study App

This is an website used for the creation, studying, and storage of flashcards and notes  
	
## Installation 

clone the https://github.com/EtienneDevictor/Team-1 git repository

create and enviroment variable and pip install
- flask
- flask_login
- flask_wtf
- flask_sqlalchemy
- xhtml2pdf
- markdown
- mkdocs

	
## Project Layout

### run.py 

This file simply runs the application
	
### app

###### __init__.py

initializes the python library and creates the app object
sets path to storage folders for images and markdown files
init also contains the app configurations and login manager

###### forms.py	
[Class SignInForm()](/forms/#class-signinform) <br>
[Class LoginForm()](/forms/#class-loginform) <br>
[Class ClassCreator()](/forms/#class-classcreators) <br>
[Class ListCreator()](/forms/#class-listcreator) <br>
[Class createFlashCardForm()](/forms/#class-createflashcardform) <br>
[Class fTextInFileForm()](/forms/#class-ftextinfileform) <br>
[Class uploadNotes()](/forms/#class-uploadnotes) <br>
[Class FlashCardForm()](/forms/#class-flashcardform) <br>
[Class QuizForm()](/forms/#class-quizeform) <br>
[Class ShareClassForm()](/forms/#class-shareclassform) <br>

###### models.py
[Class Users()](/model/#class-user) <br>
[Class Class()](/model/#class-class) <br>
[Class Notes()](/model/#class-notes) <br>
[Class Cardlist()](/model/#class-cardlist) <br>
[Class FlashCard()](/model/#class-flashcard) <br>
	
###### routes.py
[func home()](/routes/#func-home) <br>
[func delete()](/routes/#func-delete) <br>
[func signup()](/routes/#func-signup) <br>
[func login()](/routes/#func-login) <br>
[func find()](/routes/#func-find) <br>
[func create(list_id)](/routes/#func-createlist_id) <br>
[func view(list_id)](/routes/#func-viewlist_id) <br>
[func notes(class_id)](/routes/#func-notesclass_id) <br>
[func viewnotes(class_id)](/routes/#func-viewnotesclass_id) <br>
[func opener(name)](/routes/#func-openername) <br>
[func logout()](/routes/#func-logout) <br>
[func class_selector()](/routes/#func-class_selector) <br>
[func inside_class(class_id)](/routes/#func-inside_classclass_id) <br>
[func flashlist(list_id)](/routes/#func-flashlistlist_id) <br>
[func quiz(list_id, question num)](/routes/#func-quizlist_idquestion-num) <br>
[func up(num, length)](/routes/#func-upnum-length) <br>
[func down(num, length)](/routes/#func-downnum-length) <br>
[func share_class(class_id)](/routes/#func-share_classclass_id) <br>


###### mdFiles

this folder stores all the mdfiles that user uploads as notes in the [notes(class_id)](/routes/#func-notesclass_id) method in the [routes.py](/routes) file. this folder should only ever contain markdown files

###### static/images 

this folder stores all the images that user upload when creating flashcards in the [create(list_id)](/routes/#func-createlist_id) method in [routes.py](/routes) file. this folder should only ever contain jpegs

###### templates

this folder contains all the html files that are refereced in render_template call in the [routes.py](/routes) file


​	