from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    profile_pic_path = db.Column(db.String())
    bio = db.Column(db.String(255))
    comment = db.relationship('Comment', backref='user', lazy='dynamic')
    password_hash = db.Column(db.String(255))
    pitches = db.relationship('Pitch', backref='user', lazy='dynamic')
    

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'

class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    pitch = db.Column(db.String)
    category = db.Column(db.String(255))
    description = db.Column(db.String(255))
    comments = db.relationship('Comment',backref = 'pitch',lazy="dynamic")
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls,category):
        pitches = Pitch.query.filter_by(category).all()
        return pitches

    # @classmethod
    # def get_pitch(cls,id):
    #     pitch = Pitch.query.filter_by(id=id).first()

    #     return pitch
    # def save_pitch(self):
    #     db.session.add(self)
    #     db.session.commit()

        
    def __repr__(self):
        return f'Pitch {self.post}'

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    
    comment = db.Column(db.String(255))
    user_id = db.relation(db.Integer,db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,pitch_id):
        comments = Comment.query.filter_by(pitch_id=pitch_id).all()

        return comments

    def __repr__(self):
        return f'Comment:{self.comment}'