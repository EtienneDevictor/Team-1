from app import db
from app import login
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    flashCard = db.relationship('CardList', backref='author', lazy='dynamic' )
    is_active = False

    def __repr__(self):
        return f'<User { self.username }>'

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
  
class CardList(UserMixin, db.Model) :
    __tablename__ = 'cardlists'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    title = db.Column(db.String(256), index=True)
    flashCard = db.relationship('FlashCard', backref='author', lazy='dynamic')
 
    def __repr__(self):
        return f'{self.title}'

class FlashCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cardList_id = db.Column(db.Integer, db.ForeignKey('cardlists.id'))
    title = db.Column(db.String(256), index=True)
    content = db.Column(db.String(256), index=True)
    imagePath = db.Column(db.String(128), index=True)
    
    def __repr__(self):
        return self.title
    
     
 


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

