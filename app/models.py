from app import db
from app import login
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(128), index=True, unique=True)
	password_hash = db.Column(db.String(128))
	is_active = False

	def __repr__(self):
		return f'<User { self.username }>'

	def username_exists(self, username):
		for user in User:
			if (username == user.username):
				return True
		return False

	def email_exists(self, email):
		for user in User:
			if (email == user.email):
				return True
		return False

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

