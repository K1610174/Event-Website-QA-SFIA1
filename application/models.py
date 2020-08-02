from application import db
from application import login_manager
from flask_login import UserMixin


class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(30), nullable=False)
    event_date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(500), nullable=False, unique=True)

    #details = db.relationship('Users', secondary='event_details', backref=db.backref('details',lazy='dynamic'))

    #def __repr__(self):
            #return '<Events: {}>'.format(self.body)




@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))
        
class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)


    #def __repr__(self):
            #return '<Users: {}>'.format(self.body)

class Event_Details(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        user_id= db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
        event_id= db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)


