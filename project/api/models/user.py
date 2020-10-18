from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from project import db, bcrypt
from project.api.models.farm import FarmModel

class UserModel(db.Model):
    __tablename__ = '_user'
    iduser = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), nullable=False)
    fullname = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    isproprietary = db.Column(db.Boolean, default=False)
    # farms = relationship('FarmModel', secondary='work')

    def __init__(self, email, fullname, password, isproprietary):
        self.email = email
        self.fullname = fullname
        self.password = bcrypt.generate_password_hash(password).decode()
        self.isproprietary = isproprietary

    def to_json(self):
        return {
            'idUser': self.iduser,
            'email': self.email,
            'fullname': self.fullname,
            'password': self.password,
            'isProprietary': self.isproprietary
        }
