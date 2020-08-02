from application import db
from application.models import Events, Organisers

db.drop_all()
db.create_all()
