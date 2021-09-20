from flask_login import UserMixin, current_user, LoginManager
import uuid
from datetime import datetime as dt 
from werkzeug.security import check_password_hash, generate_password_hash
from app import db, login_manager
from flask_sqlalchemy import SQLAlchemy

import secrets

db = SQLAlchemy()
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id): 
    return User.query.get(user_id)



class User(UserMixin, db.Model): 
    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.string(50))
    last_name = db.Column(db.string(50))
    email = db.Column(db.string(50), unique= True)
    password = db.Column(db.string(200))
    date_created = db.Column(db.DateTime(), default=dt.utcnow)
    token = db.Column(db.String, unique=True)
    character = db.Column(db.relationship('Character', backref = 'Owner', lazy = True))


    def set_token(self, length): 
        return secrets.token_hex(length)

    def set_id(self): 
        return str(uuid.uuid4())

    def create_password_hash(self, new_password):
        self.password = generate_password_hash(new_password)

    def check_password(self, current_password):
        return check_password_hash(self.password, current_password)

    def save(self):
        self.create_password_hash(self.password)
        db.session.add(self)
        db.session.commit()

    def from_dict(self, data):
        print(data)
        for field in ['first_name' 'last_name', 'email', 'password']:
            if field in data:
                setattr(self, field, data[field])


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.string(50))
    description = db.Column(db.text)
    appeared_in = db.Column(db.text)
    super_powers = db.Column(db.text)
    date_created = db.Column(db.DateTime(), default=dt.utcnow)
    owner = db.Column(db.String, db.ForeignKey('user.token'))

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def set_id(self): 
        return secrets.token_urlsafe()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
