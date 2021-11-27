# Models 

## Class User()

​    	User table that stored login info about every user 

​		 and includes a many to many relationship to Class table   

#### Functions 

###### __repr__(self) 
    returns the username of the User
    
            Parameters:
                    self - User 
    
            Returns:
                    The username of the User

###### check_password(self, password)

	checks if the password hash is equal to the User password_hash
	
		Parameters:
				self-User
				password- the strings who hash is to be compared to password_hash
		
		returns:
				True if the password match; False otherwise

###### set_password(self, password)

	sets password_hash to the hash for password String
		
		Parameters:
				self-User
				password- A string whos hash is to be stored in password hash

## Class Class()

Table that stores all data relating to class. This table has a many to many relationship with User() and a one to many relationship with Notes() and Cardlist()

#### Functions 
	returns the title of the Class
	
	    Parameters:
	            self - Class
	
	    Returns:
	            The title of the Class
## Class Notes()

#### Functions 
	returns the title of the Notes
	
	    	Parameters:
	         		self - Notes 
	
	  	  	Returns:
	            	The title of the Notes
## Class Cardlist()

#### Functions 
	returns the title of the Cardlist
	
	   	 	Parameters:
	            	self - Class 
	
	    	Returns:
	            	The title of the Cardlist
## Class FlashCard()

### Functions 
	returns the title of the FlashCard
	
	    Parameters:
	            self - FlashCard
	
	    Returns:
	            The title of the FlashCard