from app import db
from app import login
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

classes = db.Table('classes',
                   db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                   db.Column('class_id', db.Integer, db.ForeignKey('class.id'))
)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    classes = db.relationship('Class', secondary=classes, backref=db.backref('users'), lazy='dynamic')
    todo = db.relationship('Todolist', backref='author', lazy='dynamic', cascade='all, delete-orphan')

    def __repr__(self):
        return f'{ self.username }'

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

class Todolist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rank = db.Column(db.Integer)
    title = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __repr__(self):
        return f'{self.rank}, { self.title }'
      
class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True)
    cardlist = db.relationship('Cardlist', backref='author', lazy='dynamic')
    notes = db.relationship('Notes', backref='author', lazy='dynamic')
    active_class = None
    
    def __repr__(self):
        return f'{self.title}'
    
    def set_class_to_active(self, class_id):
        active_class = class_id
    
    def active_class(self):
        return self.active_class
        
    
class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey('class.id'))
    title = db.Column(db.String(128), index=True)
    mdFilePath = db.Column(db.String(128), index=True)
    
    def __repr__(self):
        return f'{self.title}'
     
class Cardlist(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey('class.id'))
    title = db.Column(db.String(128), index=True)
    flashCard = db.relationship('FlashCard', backref='author', lazy='dynamic')
 
    def __repr__(self):
        return f'{self.title}'
    
class FlashCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cardList_id = db.Column(db.Integer, db.ForeignKey('cardlist.id'))
    title = db.Column(db.String(256), index=True)
    content = db.Column(db.String(256), index=True)
    imagePath = db.Column(db.String(128), index=True)
    
    def __repr__(self):
        return f'{self.title}'
    
     
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

