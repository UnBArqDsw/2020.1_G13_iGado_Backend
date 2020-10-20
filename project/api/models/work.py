from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from project import db
from project.api.models.user import UserModel
from project.api.models.farm import FarmModel

class WorkModel(db.Model):
    __tablename__ = 'work'
    user_id = db.Column(db.Integer, db.ForeignKey('_user.user_id'), nullable=False, primary_key=True)
    farm_id = db.Column(db.Integer, db.ForeignKey('farm.farm_id'), nullable=False, primary_key=True)

    def __init__(self, user_id, farm_id):
        self.user_id = user_id
        self.farm_id = farm_id