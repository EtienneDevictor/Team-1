# Routes

## func home()

renders home.html template
	
returns:
	rendering of home.html

## func delete()

takes in the login and password of a user and removes [Users()](/model/#class-user) from the database

returns: 
        rendering of delete.html with [LoginForm()](/forms/#class-loginform) <br>

## func signup()

takes in user entered info to create a [Users()](/model/#class-user) object in and enters it into the database
	
returns: rendering of signup.html with [SignInForm()](/forms/#class-signinform) <br>

## func login()

takes in user entered information to check [Users()](/model/#class-user) object and matches with database. After verification, logs the user in or denies request

returns: rendering of login.html with [LoginForm()](/forms/#class-loginform)

## func find()

takes in text entered by user and prints all flashcards in the [Users()](/model/#class-class) with the text inside their content

returns:
        rendering of viewflashcards.html with [fTextInFileForm()](/forms/#class-ftextinfileform) <br>   

## func create(list_id)

takes in information from the user to create [FlashCard()](/model/#class-flashcard) object that is linked to a provided [Cardlist()](/model/#class-cardlist)
	
parameters:
		list_id: unique identification number of the list that the flashcard object will be linked to
			
returns:
		rendering of createflashcard.html with [createFlashCardForm()](/forms/#class-createflashcardform) form attached

## func view(list_id)

returns a list view of all the  [FlashCard()](/model/#class-flashcard) contained with a provided [Cardlist()](/model/#class-cardlist). Images contained in cards are not displayed in list view
	
parameters:
		list_id: unique identification # of the list obj containing specified flashcards
			
returns:
		a rendering of viewflashcard.html with a list of flashcards in list with id=list_id

## func notes(class_id)

takes in user entered information to create a [Notes()](/models/#class-notes) object and saves it to the database

parameters:
		class_id: unique identifacation # of the class object containing specified notes

returns: renders uploadnotes.html with [uploadNotesForm()](/forms/#class-uploadNotesForm) form 


## func viewnotes(class_id)

returns a list view of all [Notes()](/model/#class-notes) in a specified class_id and the ability to use [converter(name)](/routes/#func-convertername) or upload new [uploadNotesForm()](/forms/#class-uploadNotesForm)

parameter:
		class_id: unique identifacation # of the class object containing specified notes

returns: renders viewnotes.html with a list of notes in specified class_id

## func opener(name)

takes in the specified [Notes()](/model/#class-notes) selected and converts the file into a viewable html and displays it

parameter:
		name = unique identifier for specified Notes()(/model/#class-notes)

returns: renders base.html and the [Notes()](/model/#class-notes) attached

## func logout()

logs user out then redirects to login page.

returns: renders login.html 

## func class_selector()

provides a list of the active users classes that they can pick to open or can take in user inputted data to create a new [Class()](/model/#class-class) object
	
returns:
        a rendering of of class.html with a list of classes and the [ClassCreator()](/forms/#class-classcreators) form

## func inside_class(class_id)

provides a list of notes and flashcard lists contained within the class and links to creating new notes and form to create a new [Cardlist()](/model/#class-cardlist) object

parameters:
		class_id: the unique identification number of the [Class()](/model/#class-class) object whose [Cardlist()](/model/#class-cardlist)and [Notes()](/model/#class-notes)  objects are to be listed
		
returns:
		rendering of inside_class.html with list of flashcards and notes and a [ListCreator()](/forms/#class-listcreator)


## func flashlist(list_id, card_id)

provides a flashcard view of flashcard in specified list with a form to flip and change flashcard; also provides a link to switch to list [view(list_id)](/routes/#func-viewlist_id) and to [create(list_id)](/routes/#func-createlist_id) flashcard

parameters:
		list_id: the unique identification number of the [Cardlist()](/model/#class-cardlist) object 
		card_id: the unique identification number of the [FlashCard()](/model/#class-flashcard) object to be viewed
		
returns:
		rendering of flashcards.html with [FlashCardForm()](/forms/#class-flashcardform) and specified flashcard

## func quiz(list_id,question_num)

creates the form [QuizForm()](/forms/#class-quizform) and collects the user submitted answers

parameters:
        list_id: the unique identification number of the [Cardlist()](/model/#class-cardlist) object
        question_num: variable to keep track of the question number for the quiz form

returns: 
        renders quiz.html with the [QuizForm()](/forms/#class-quizform)
        when submitted, redirects to [show_answers(list_id)](/routes/#func-show_answerslist_id) and flashes the number of questions answered correctly

## func up(num, length)
increments the question number by 1 if it is less than the length to move through the [QuizForm()](/forms/#class-quizform)

parameter:
        num: int variable to represent the question number
        length: int variable to represent the total number of quiz questions

returns:
        if num equals length, returns length, otherwise returns num + 1

## func down(num, length)
decrements the question number by 1 if it is greater than 0 to move through the [QuizForm()](/forms/#class-quizform)

parameters:
        num: int variable to represent the question number
        length: int variable to represent total number of quiz questions
returns: 
        if num is equal to 0, returns 0, otherwise returns num - 1

## func share_class(class_id)

provides a form to that takes user inputted data to give access to another user for a class that they have access to 

parameters:
		class_id: the unique identification # of the [Class()](/model/#class-class) that is to be shared 
		
returns: 
		a rendering of shareclass.html with the [ShareClassForm()](/forms/#class-shareclassform)

##func show_answers(list_id):

generates the questions, user responses, and correct responses to the quiz submitted in [quiz(list_id,question_num)](/routes/#func-quizlist_idquestion_num)

parameters:
        list_id: the unique identification number of the [Cardlist()](/model/#class-cardlist) object

returns:
        rendering of quizanswers.html displaying the quiz questions, user's response to those question, and the correct responses to the questions
