from flask_login import UserMixin, current_user
from datetime import datetime as dt 
from werkzeug.security import check_password_hash, generate_password_hash
from app import db, login_manager

class Character(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.string(50))
    description = db.Column(db.text)
    appeared_in = db.Column(db.text)
    super_powers = db.Column(db.text)
    date_created = db.Column(db.DateTime(), default=dt.utcnow)
    # owner = foreign key to User using the user's token

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
