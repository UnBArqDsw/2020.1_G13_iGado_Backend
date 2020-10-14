from sqlalchemy.sql import func

from project import db

class FarmModel(db.Model):
    __tablename__ = 'farm'
    idFarm = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idProprietary = db.Column(db.Integer, db.ForeignKey('proprietary.idProprietary'), nullable=False)

    def __init__(self):
        None