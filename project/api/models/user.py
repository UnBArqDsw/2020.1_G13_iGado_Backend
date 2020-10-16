from sqlalchemy.sql import func

from project import db
from project.api.models.farm import FarmModel

class UserModel(db.Model):
    __tablename__ = '_user'
    iduser = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), nullable=False)
    fullname = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    isproprietary = db.Column(db.Boolean, default=False)
    farms = db.relationship('FarmModel', backref=db.backref('_user'), lazy=True)

    def __init__(self, email, fullname, password, isProprietary):
        self.email = email
        self.fullname = fullname
        self.password = password
        self.isProprietary = isProprietary
