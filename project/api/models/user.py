from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from project import db

class UserModel(db.Model):
    __tablename__ = '_user'
    idUser = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), nullable=False)
    fullname = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    isProprietary = db.Column(db.Boolean, default=False)
    # farms = relationship('FarmModel', secondary='work')

    def __init__(self, email, fullname, password, isProprietary):
        self.email = email
        self.fullname = fullname
        self.password = password
        self.isProprietary = isProprietary
    
    def to_json(self):
        return {
            'idUser': self.idUser,
            'email': self.email,
            'fullname': self.fullname,
            'password': self.password,
            'isProprietary': self.isProprietary
        }
