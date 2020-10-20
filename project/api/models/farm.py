from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from project import db


class FarmModel(db.Model):
    __tablename__ = 'farm'
    farm_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    size_farm = db.Column(db.Integer, nullable=False)
    users = relationship('UserModel', secondary='work')

    def __init__(self, size_farm):
        self.size_farm = size_farm
