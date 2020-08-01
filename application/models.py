from application import db
from application import login_manager
from flask_login import UserMixin
from sqlalchemy.orm import relationship, backref


event_details= db.Table('event_details',
        db.Column('id',db.Integer,primary_key=True,autoincrement=True),
        db.Column('user_id',db.Integer, db.ForeignKey('users.id'),nullable=False),
        db.Column('event_id',db.Integer, db.ForeignKey('events.id'),nullable=False)
        )

class Events(db.Model):
    __tablename__='events'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_name = db.Column(db.String(30), nullable=False)
    event_date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(500), nullable=False, unique=True)

    users = db.relationship('Users', secondary='event_details' )

    def __repr__(self):
            return '<Events: {}>'.format(self.body)


@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))
        
class Users(db.Model, UserMixin):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)

    events = db.relationship('Events', secondary='event_details' )

    def __repr__(self):
            return '<Users: {}>'.format(self.body)

class Event_Details(db.Model):
    __tablename__ = 'event_details'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'))

    users = db.relationship(Users, backref=backref('event_details', cascade="all, delete-orphan"))
    events = db.relationship(Events, backref=backref('event_details', cascade="all, delete-orphan"))

    def __repr__(self):
            return '<Event Details: {}>'.format(self.body)

