from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FieldList, FormField
from flask_wtf.file import FileField, FileAllowed
from wtforms import validators
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired, NumberRange

class SignInForm(FlaskForm):
    username = StringField('User', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

    register = SubmitField('Sign up')
        
class LoginForm(FlaskForm):
    username = StringField('User', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')

    submit = SubmitField('Login')
    delete = SubmitField('Delete Account')
    
class ClassCreator(FlaskForm):
    title = StringField('Enter new Class Name', validators=[DataRequired()])
    submit = SubmitField('Create new Class')
    
class ListCreator(FlaskForm):
     title = StringField('Enter New FlashCard List Name', validators=[DataRequired()])
     submit = SubmitField('Create new FlashCard List')
 
class createFlashCardForm(FlaskForm):
    title = StringField('Title of the Card', validators=[DataRequired()])
    image = FileField('Image File (jpg only)', validators=[FileAllowed(['jpg'])])
    text = StringField('Text inside the flashcard', widget=TextArea())
    front = BooleanField('Image on the front of the flash card')
    create = SubmitField('Create FlashCard')

class fTextInFileForm(FlaskForm):
    text = StringField('Enter text to search for flashcard', validators=[DataRequired()])
        
    find = SubmitField('Find FlashCard') 

class uploadNotes(FlaskForm):
    title = StringField("Title of the Notes", validators = [DataRequired()])
    notes = FileField('Notes (.md format)', validators = [FileAllowed(['md'])])
    save = SubmitField('Save notes')
    
class FlashCardForm(FlaskForm):
    next = SubmitField('Next')
    previous = SubmitField('Previous')

    flip = SubmitField('Flip')
    
class QuizForm(FlaskForm):
    answer = StringField('Answer', validators = [DataRequired()])
    next = SubmitField('Next')
    previous = SubmitField('Previous')
    submit = SubmitField('Submit')
    
class ShareClassForm(FlaskForm):
    username = StringField('Enter the name of the user you wish to share this list with', validators = [DataRequired()])
    share = SubmitField('Share')  
    
class ToDoListForm(FlaskForm): 
    title = StringField('To Be Completed', validators = [DataRequired()]) 
    rank = StringField('Priority Level', validators = [DataRequired(), NumberRange(min=1, max=10, message='Invalid Rank')])
    insert = SubmitField('Insert in List')
