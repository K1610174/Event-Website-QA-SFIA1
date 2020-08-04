from application import db

class Events(db.Model):
    event_id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(30), nullable=False)
    event_date = db.Column(db.DateTime, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    org_details = db.relationship('Event_Details',backref='organiser',lazy=True)

    def __repr__(self):
        return ''.join([
            'Event ID: ', str(self.event_id), '\r\n',
            'Date: ', self.event_date, '\r\n',
            'Name: ', self.event_name, ' ', self.description, ' ', self.location
        ])

class Organisers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    event_deets = db.relationship('Event_Details',backref='event',lazy=True)
    
    def __repr__(self):
        return ''.join([
            'Organiser ID: ', str(self.id), '\r\n',
            'Email: ', self.email, '\r\n',
            'Name: ', self.first_name, ' ', self.last_name
        ])

class Event_Details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer,db.ForeignKey('events.event_id'), nullable=False)
    organiser_id = db.Column(db.Integer,db.ForeignKey('organisers.id'), nullable=False)
