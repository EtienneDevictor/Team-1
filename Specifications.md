
## Team-1 Study-Better 
[Github Project Link](https://github.com/EtienneDevictor/Team-1)
# Use Case Desciption
**Date: 9/15/2021**

**Product Name: Study-Better**

**Problem Statement: Creating an app to help user study using customizable flashcards and notes**

**Non-functional Requirements**
* System should respond to the user withing one second 
* All text communicated to the user shall be in english 
* This application should only access .md and .png files


**Login/Sign-up**

## Summary

The user of the program logins in with a preexisting account if the user does not already have an account they will be asked to sign up

## Actors

1. The user

## Preconditions 

* None

## Trigger 

The User enter the Login Page

## Primary Sequence

1. User enters username into username textbox
2. User enter password into password textbox
3. User hit enter key or clicks login button
4. Verify the the username corresponds to existing account 
5. Verify that password matches username

## Primary Postcondition

* user is logged into account

## Alternate Sequences

User choices to click on sign up button 

1. user enters personal information into designated text boxes 
2. User enter username and password into designated textboxes 
3. User clicks signup

step 4 fails

1. launch error message "no such username exists"
2. user goes back to step 1

step 5 fails

1. launch error message "password does not match username"
2. user goes back to step 1

## Alternate Postcondition 

user creates an account and is logged into account


**Input a markdown file and output flashcards**

## Summary

The user of the program inputs a markdown file and it will then convert it and save it into flashcards for the user to access. 

## Actors

1. The user

## Preconditions

* The user is logged in
* The user is providing a markdown file 

## Trigger

The user clicked on the import markdown file

## Primary Sequence

1. User clicks on import markdown file
2. User selects markdown file
3. System converts markdown file to flash cards
4. User can then save and access flashcards

## Primary Postcondition

* The user has access to the saved flashcards

## Alternate Sequences

1. User selects a file that is not a markdown file
2. User clicks on import markdown file
3. User selects invalid file type
4. Send error message “file is not compatible, Please select a markdown file”
5. User goes back to step 2

## Alternate Postcondition

* None


**Use pomodoro timer**

## Summary

The user decides on a task, starts a countdown timer, after a given time the timer will notify the user to take a small break. Every 4 breaks, the timer will make the user take a longer break

## Actors

1. The user

## Preconditions

* None

## Trigger

The user clicked on the pomodoro timer app

## Primary Sequence

1. User will input their task
2. Click the start timer for the main timer
3. After 25 minutes of working on their task, the timer will notify the user to take a break, if this is the 4th break, jump to step 7
4. Click to start the short break timer
5. After 5 minutes the timer will notify the user to continue working on the task
6. Repeat back to step 2
7. Navigate to the long break timer
8. Set the duration (between 15-30 minutes) and start the long break 
9. After 15-30 minutes, the timer will notify user to continue working on the task
10. Repeat back to step 2

## Primary Postcondition

* User is satisfied with their study time

## Alternate Sequences

* None

## Alternate Postcondition

* None


**Add todo tracker**

## Summary

User will be able to input tasks they want to complete as well as check off completed tasks

## Actors

1. The user

## Preconditions

* The user is logged in

## Trigger

The user clicked on the todo tracker app

## Primary Sequence

1. User enters tasks 
2. User sets goals
3. User saves tasks
4. System provides list of tasks
5. User clicks completed tasks
6. Tasks are removed

## Primary Postcondition

* The user is able to access the todo tracker and check tasks off

## Alternate Sequences

* None

## Alternate Postcondition

* None


**Forums section**

## Summary

Users can access a forums section that will allow users to post questions for other peers to answer as well as have an archive of answered questions

## Actors

1. The user
2. Other users

## Preconditions

* The user must be logged in

## Trigger

The user clicked on the forums app

## Primary Sequence

1. User searches up their problem
2. System goes through archive to match similar problems
3. User selects similar problem
4. User can view and reply to forum

## Primary Postcondition

* None

## Alternate Sequences

User is unable to find similar forum post, posts a questions 
1. User searches up their problem
2. System goes through archive to match similar problems
3. User is unsatisfied with current results
4. Clicks new posts
5. User inputs title
6. User inputs description of problem
7. User clicks post

User wants to answer forum posts
1. User clicks on forum title
2. System provides information on problem
3. User can navigate to the bottom and inputs their thoughts into text box
4. Click share button

## Alternate Postcondition

* Everyone can see the posts made


**Searching files for file containing specific text**

## Summary

this use case searches all the user notes and flashcards for specific words or phrases and returns a list of flashcards and notes files to the user and the user can choose one to open and look through themselves.

## Actors

1. The user 

## Preconditions 

* the user is logged into there account 
* the user is on the notes/flashcard directory page

## Trigger

The user enters a series of words or phrases into the text box labeled as the trigger 

and enters the words and phrases (denoted by surrounding "") and presses enter.

## Primary Sequence

1. the user clicks enter after having filled out the textbox
2. the app parses through all saved files attempting to find the note and flashcard files 
3. the app returns a list of the file names that contained the searched for phrases
4. user clicks on the file they wish to open 
5. they app displays the list of flashcards displayed in the file

## Primary Postcondition 

the user has a opened flashcard/notes file that contained the searched for phrases

## Alternate Sequence

The app fails to find the phrase in step two

1. the app launches a no such phrase exist in notes error message

## Alternate Postcondition

the user stays on the files directory because the phrase was not found 



**Converting markdown files to downloadable pdf** 

## Summary

Convert markdown files like the note and flashcard files to pdf so that that the user can download them to the device

## Actor

1. the user

## Preconditions

* the user is logged in 
* the user has added the md file to collection 
* the user is on the notes/flashcard directory page

## Trigger 

The user clicks on download file button on the notes/flashcard directory page

## Primary Sequence

1. The user clicks on the download a file button 
2. the system prompts the user to select a file for download
3. the system find the desired file in the account files saves
4. The system converts the file to a pdf
5. the system offloads the pdf into the users downloads folder Postcondition

## Postconditions

the user had downloaded the file as a pdf onto their device



**Transferring notes between users**

## Summary
A user get a markdown file from the system transfers the file to another user who inputs it and gets a set of notes added to their account


## Actors

1. user 1 
2. user 2

## Preconditions 

* user 1 has made a note file
* user 1 is logged in 
* user 1 currently has the set of notes opened 
* user 2 is logged in 
* user 2 is currently on the flashcard/notes explorer page

## Trigger 

user 1 clicks on the share button located on screen

## Primary Sequence

1. User 1 clicks on the share button
2. a pop up tab appears with a  markdown file linked to it
3. user 1 downloads the markdown file
4. user 1 transfers the markdown file to user 2
5. user 2 clicks on create notes button
6. system open tab with two buttons one to create from scratch on to input file
7. user 2 click input file button
8. user 2 is prompted to insert the file
9. user 2 inserts the file
10. the file is verified as a working flashcard file 
11. the markdown file is converted into flashcards a
12. notes outputted to user 2

## Primary Postcondition
The notes that user 1 transferred can now be viewed and edited on user two account with out affecting the notes on user ones account

## Alternate Sequences

Step 9 fails
1. user 2 is sent back to step 6



**Transferring Flashcards Between Users**

## Summary
a user gets markdown file from the system, transfers it to another user and the second user inputs it into system and the flashcards are added to there account

## Actors

1. user 1 
2. user 2

## Preconditions 

* user 1 has made a set of flashcards 
* user 1 is logged in 
* user 1 currently has the set of flashcards opened 
* user 2 is logged in 
* user 2 is currently on the flashcard/notes explorer page

## Trigger 

user 1 clicks on the share button located on screen

## Primary Sequence

1. User 1 clicks on the share button
2. a pop up tab appears with a  markdown file linked to it
3. user 1 downloads the markdown file
4. user 1 transfers the markdown file to user 2
5. user 2 clicks on create flashcards button
6. system open tab with two buttons one to create from scratch on to input file
7. user 2 click input file button
8. user two is prompted to insert the file
9. the file is verified as a working flashcard file 
10. the markdown file is converted into flashcards and outputted to user 2

## Primary Postcondition
The flash cards that user 1 transferred can now be viewed and edited on user two account without affecting the cards on user ones account

## Alternate Sequences

Step 9 fails to be verified
1. user 2 is sent back to step 6

**Use Case Name: Quiz Feature**
## Summary
The user will be able to access a quiz feature for a subject or course. Upon being accessed, questions are prompted based on the subject or course they chose to promote learning.  
## Actors
The user 
## Preconditions
* user is logged into account
* the user has flashcards 
*notes are sorted by class or categories
 
## Triggers
The user clicks on the “Quiz” button. The user is brought to the quiz page and the quiz begins.  
## Primary Sequence
1. User clicks on the quiz button
2. User inputs an answer to the first question
3. User is ready to move onto the next question
4. User can press the “next” button to move onto the next question
5. User continues step 3 and 4 until there are no more questions 
6. User presses the “submit” button
7. The quiz is submitted and is automatically graded
8. Program displays a grade and an option for the user to review their answers
9. The user can go forward through the questions by pressing the “next” button
10. The user’s answers are displayed and the correct answers are displayed, if they got the question wrong
## Primary Postconditions
* user completes the quiz
 
## Alternate Sequences
* Step 5 alt. seq.
1. User wants to go back to a previous question
2. User can press the “previous” button to move back to the previous question

* Step 9 alt. seq.
1. User can go backward through the questions by pressing the “previous” button

* Step 2 alt. seq.
1. User can exit the quiz at anytime
### Alternate Postconditions
* if user exits the quiz, the user does not need to complete the quiz

**Use Case Name: Sort notes by Class or Category**
## Summary
The user can separate notes by class or category. This will make it easier for the user to sort through their notes and will function to save time for the user. 
## Actors
1. The user
## Preconditions
* The user has an account
* The user can have notes already created
## Triggers
*User clicks on one of the notes and can drag it to a class or category
*User can create a note and select to create it in a class or category 
 
## Primary Sequence
1. The user creates a new class or category inside the notes pages
2. The user can drag their notes into the newly created class or categories
3. The user can sort the class or categories into any order

## Primary Postconditions
* The user has a new class or category
* The user has notes inside the class or category 
## Alternate Sequences
* Step 2 alt. Seq.
1. The user can create new notes
2. The user selects the class or category to add the notes into
* Step 1 alt. Seq.
1. The user can remove class or category inside the notes pages
### Alternate Trigger
1. The user is editing the notes
1. The user can change the class or category of the notes
### Alternate Postconditions
1. The user has no classes or categories
 
**Use Case Name: Render markdown notes**
## Summary
The user enters text in the markdown format, and the syntax should render the notes changing the appearance of the text as it is entered. 
## Actors
1. User 1 
## Preconditions
* The user enters text in the markdown syntax
## Triggers
The user enters text in the markdown syntax, and the app should correctly render the typed input to the proper output
## Primary Sequence
1. User 1 opens the notes
2. User 1 enters the text into his notes
3. User 1 saves the notes
4. The notes are correctly rendered in the markdown file
## Primary Postconditions
* Notes are correctly rendered in the markdown format
 
**Use Case Name: Create groups and add group chat**
## Summary
The user can create groups of people to share/edit notes and chat online via a text channel
 
## Actors
1. User 1
2. User 2
3. User 3
## Preconditions
* All users have an account and are signed in
* One user must have a note page open to share or edit
## Triggers
User 1 decides to share notes with users for them to view/edit. A group is created and the users can edit the notes and a text channel is created so that the members of the group can chat amongst each other. 
 
## Primary Sequence
1. User 1 goes to the main page
2. User 1 clicks the “create group” button
3. User 1 can send a group invitation to User 2 and User 3
4. User 2 and User 3 join the group
5. User 1, 2, and 3 can create a new note
6. User 1, 2, and 3 can edit the note
7. User 1, 2, and 3 can chat in the text channel to update each other
 
## Primary Postconditions
* Users 1, 2, and 3 are in a group together
* Users 1, 2, and 3 are in a chat together
* Users 1, 2, and 3 can edit notes in their group
 
## Alternate Sequences
* Step 5 alt. Seq.
1. User 1, 2, or 3 can share a note that they have already created
### Alternate Trigger
Any of the users can prompt the group creation

