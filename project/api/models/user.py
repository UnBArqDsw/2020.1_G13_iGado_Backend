from sqlalchemy.sql import func

from project import db
from project.api.models.farm import FarmModel

class UserModel(db.Model):
    __tablename__ = '_user'
    idUser = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), nullable=False)
    fullname = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    isProprietary = db.Column(db.Boolean, default=False)
    farms = db.relationship('FarmModel', backref='_user', lazy=True)

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
