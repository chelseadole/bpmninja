"""Init script."""
from flask import Flask, Blueprint
from flask_restplus import Api

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import DateTime, func, Integer

from bpmninja.bpm import bpm_ns

app = Flask(__name__)
app.config['RESTPLUS_VALIDATE'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

api = Api(version='1.0',
          title='BPM Ninja API',
          description='A simple flask API to handle the backend of bpmninja'
          )


def initialize_app():
    """Initialize bpmninja API flask app. Register ns (namespaces) and blueprints."""

    # Register all API namespaces:
    api.add_namespace(bpm_ns, path='/bpm')

    bp = Blueprint('api', __name__, url_prefix='/api/v1')
    api.init_app(bp)

    app.register_blueprint(bp)


def initialize_db():
    """Init DB models/instance."""
    db = SQLAlchemy(app)

    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80), unique=True, nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)
        password = db.Column(db.String(30), nullable=False)
        allScores = db.Table('scores',
                             db.Column('date', DateTime, default=func.now()),
                             db.Column('score', Integer),
                             db.Column('high', Integer),
                             db.Column('low', Integer),
                             nullable=True
                             )
        avgScore = db.Column(db.Integer)
        highScore = db.Column(db.Integer)

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

    db.create_all()

    new_user = User(username='test1', email='test@gmail.com', password='welcome1', avgScore=30, highScore=80)
    db.session.add(new_user)
    db.session.commit()
    print(User.query.all())


if __name__ == '__main__':
    initialize_app()
    app.run(host='127.0.0.1', port=5000, debug=True)
