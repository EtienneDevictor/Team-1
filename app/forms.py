from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FileField, validators
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
 
class createFlaskCard(FlaskForm):
	title = StringField('Title of the Card', validators=[DataRequired()])
	image = FileField(u'Image File (jpg only)', [validators.reqexp(u'^[/\\]\.jpg$')])
	text = StringField('Text inside the flashcard')
	front = BooleanField('Image on the front of the flash card')
	create = SubmitField('Create FlashCard')
