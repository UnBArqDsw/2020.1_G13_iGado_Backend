from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from project import db

class FarmModel(db.Model):
    __tablename__ = 'farm'
    idFarm = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sizeFarm = db.Column(db.Integer, nullable=False)
    # users = relationship('UserModel', secondary='work')

    def __init__(self, sizeFarm):
        self.sizeFarm = sizeFarm
