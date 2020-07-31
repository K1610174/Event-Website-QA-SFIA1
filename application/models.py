from application import db
from application import login_manager
from flask_login import UserMixin



class Events(db.Model):
    __tablename__='event'
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(30), nullable=False)
    event_date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(500), nullable=False, unique=True)
    event_details = db.relationship('EventsDetails', backref='event', lazy=True)

    def __repr__(self):
        return ''.join([
            'Event: ',str(self.id),' ', self.event_name, ' ', self.event_date, '\r\n',
            'Title: ', self.location, '\r\n', self.description
            ])


@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))
        
class Users(db.Model, UserMixin):
    __tablename__='user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(500), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)
    event_details = db.relationship('EventsDetails', backref='user', lazy=True)
    
    def __repr__(self):
        return ''.join([
            'User: ', str(self.id), '\r\n',
            'Email: ', self.email, '\r\n',
            'Name: ', self.first_name, ' ', self.last_name
        ])

class EventDetails(db.Model):
        __tablename__='event_details'
        id = db.Column(db.Integer,primary_key=True)
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
        event_id = db.Column(db.Integer, db.ForeignKey('event.id'))

        def __repr__(self):
            return '<Event Details: {}>'.format(self.id)
