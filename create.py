from application import db
from application.models import Events, Users

db.drop_all()
db.create_all()
