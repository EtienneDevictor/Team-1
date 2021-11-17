from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FieldList, FormField
from flask_wtf.file import FileField, FileAllowed
from wtforms import validators
from wtforms.validators import DataRequired

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
    title = StringField('Enter new Class Name')
    submit = SubmitField('Create new Class')
 
class createFlashCardForm(FlaskForm):
	title = StringField('Title of the Card', validators=[DataRequired()])
	image = FileField('Image File (jpg only)', validators=[FileAllowed(['jpg'])])
	text = StringField('Text inside the flashcard')
	front = BooleanField('Image on the front of the flash card')
	create = SubmitField('Create FlashCard')

class uploadNotes(FlaskForm):
	title = StringField("Title of the Notes", validators = [DataRequired()])
	notes = FileField('Notes (.md format)', validators = [FileAllowed(['md'])])
	save = SubmitField('Save notes')
