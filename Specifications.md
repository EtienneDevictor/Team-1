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



