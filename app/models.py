from app import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(128), index=True, unique=True)
	password_hash = db.Column(db.String(128))

	def __repr__(self):
		return f'<User {username}>'

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
