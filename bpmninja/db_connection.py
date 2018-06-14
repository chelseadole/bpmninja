"""DB connection spec for bpms, and users."""
from flask_sqlalchemy import SQLAlchemy
from run import app

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class BPM(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    songTitle = db.Column(db.String(300), nullable=False)
    artist = db.Column(db.String(300), nullable=False)
    album = db.Column(db.String(300), nullable=False)
    bpm = db.Column(db.Integer)

    def __repr__(self):
        return '<Song: %r>, BPM: %r' % (self.songTitle, self.bpm)