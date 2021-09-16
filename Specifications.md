# Use Case Description
** Date: 9/15/2021
** Product Name: 
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



** Searching files for file containing specific text

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




