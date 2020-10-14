from sqlalchemy.sql import func

from project import db
from project.api.models.farm import FarmModel

class ProprietaryModel(db.Model):
    __tablename__ = 'proprietary'
    idProprietary = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), nullable=False)
    fullname = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    farms = db.relationship('FarmModel', backref='proprietary', lazy=True)

    def __init__(self, email, fullname, password):
        self.email = email
        self.fullname = fullname
        self.password = password

