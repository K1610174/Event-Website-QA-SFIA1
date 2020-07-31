from application import db
from application import login_manager
from flask_login import UserMixin



class Events(db.Model):
    __tablename__='events'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    event_name = db.Column(db.String(30), nullable=False)
    event_date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(500), nullable=False, unique=True)
    event_details = db.relationship('EventsDEtails', backref='event',primaryjoin='events.id==event_details.event_id', lazy='dynamic')

    def __repr__(self):
        return ''.join([
            'Event: ',str(self.id),' ', self.event_name, ' ', self.event_date, '\r\n',
            'Title: ', self.location, '\r\n', self.description
            ])


@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))
        
class Users(db.Model, UserMixin):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    email = db.Column(db.String(500), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)
    event_details = db.relationship('EventDetails', backref='user',primaryjoin='users.id==event_details.user_id' ,lazy='dynamic')
    
    def __repr__(self):
        return ''.join([
            'User: ', str(self.id), '\r\n',
            'Email: ', self.email, '\r\n',
            'Name: ', self.first_name, ' ', self.last_name
        ])

class EventDetails(db.Model):
        __tablename__='event_details'
        id = db.Column(db.Integer,primary_key=True,autoincrement=True)
        user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
        event_id = db.Column(db.Integer, db.ForeignKey('events.id'))

        def __repr__(self):
            return '<Event Details: {}>'.format(self.id)
