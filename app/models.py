from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
from hashlib import md5
from app import app


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=monsterid&s={}'.format(
            digest, size)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)


class fileTable(db.Model):
    __tablename__ = 'filetable'

    ID = db.Column(db.Integer, primary_key=True)
    Station_Code = db.Column(db.String(200))
    Station_Name = db.Column(db.String(200))
    Location = db.Column(db.String(200))
    Month = db.Column(db.String(32))
    Day = db.Column(db.String(32))
    Year = db.Column(db.String(32))
    Weather = db.Column(db.String(200))
    PC = db.Column(db.String(200))
    Client = db.Column(db.String(200))
    Type = db.Column(db.String(200))
    Longitude = db.Column(db.String(200))
    Latitude = db.Column(db.String(200))
    isActive = db.Column(db.Boolean, unique=False, default=True)

    def __repr__(self):
        return '<fileTable {}>'.format(self.Station_Code)


class excelFile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    excel_file = db.Column(db.String(1000))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    fileTable_id = db.Column(db.Integer, db.ForeignKey('filetable.ID'))


@login.user_loader
def load_user(id):
    return User.query.get(int(id))