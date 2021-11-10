from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
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
