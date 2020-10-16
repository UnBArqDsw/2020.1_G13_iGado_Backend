from sqlalchemy.sql import func

from project import db

class FarmModel(db.Model):
    __tablename__ = 'farm'
    idFarm = db.Column(db.Integer, primary_key=True, autoincrement=True)
    iduser = db.Column(db.Integer, db.ForeignKey('_user.iduser'), nullable=False)

    def __init__(self):
        None