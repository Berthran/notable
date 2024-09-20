from datetime import datetime
from flask_login import UserMixin
from flask import current_app
from notable import db, login_manager
from notable.models.note import Note
from itsdangerous import URLSafeTimedSerializer as Serializer


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(db.Model, UserMixin):
    '''
    A user object.

    A user is someone with the First name, Last name, an email an a password
    who has create, edit and delete notes in their account.

    A user can have one or multiple notes.
    '''

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(40), nullable=False)
    lastname = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(40), nullable=False)
    image = db.Column(db.String(60), nullable=False, default="default.jpg")
    notes = db.relationship('Note', backref='author', lazy=True)

    def get_reset_token(self):
        ''' Generate time sensitive token to ensure only a specific user
        can reset password '''
        s = Serializer(current_app.config['SECRET_KEY'])
        return s.dumps({'user_id': self.id})
    
    @staticmethod
    def verify_reset_token(token):
        ''' Verifies a reset token '''
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token, max_age=1800)['user_id']
        except:
            return None
        return User.query.get(user_id)
        

    def __repr__(self):
        return f"User('{self.firstname} {self.lastname}' '{self.email}'"

