## Team-1 Study Better App
[Github Project Link](https://github.com/EtienneDevictor/Team-1)

# Login/Sign-up

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



# Input a markdown file and output flashcards

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

# Use pomodoro timer

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

# Add todo tracker

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


# Forums section

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

