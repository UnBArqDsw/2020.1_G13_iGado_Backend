from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from project import db, bcrypt
from project.api.models.farm import FarmModel

class UserModel(db.Model):
    __tablename__ = '_user'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), nullable=False)
    fullname = db.Column(db.String(128), nullable=False)
<<<<<<< HEAD
    password = db.Column(db.String(255), nullable=False)
    isproprietary = db.Column(db.Boolean, default=False)
    # farms = relationship('FarmModel', secondary='work')
=======
    password = db.Column(db.String(128), nullable=False)
    is_proprietary = db.Column(db.Boolean, default=False)
    farms = relationship('FarmModel', secondary='work')
>>>>>>> 686624a2bfc6d123a9c0d82be2311a3659332d4f

    def __init__(self, email, fullname, password, is_proprietary):
        self.email = email
        self.fullname = fullname
<<<<<<< HEAD
        self.password = bcrypt.generate_password_hash(password).decode()
        self.isproprietary = isproprietary

=======
        self.password = password
        self.is_proprietary = is_proprietary
    
>>>>>>> 686624a2bfc6d123a9c0d82be2311a3659332d4f
    def to_json(self):
        return {
            'user_id': self.user_id,
            'email': self.email,
            'fullname': self.fullname,
            'password': self.password,
            'is_proprietary': self.is_proprietary,
            'farms': [farm.farm_id for farm in self.farms]
        }

    