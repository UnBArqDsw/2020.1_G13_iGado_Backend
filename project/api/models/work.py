from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from project import db
from project.api.models.user import UserModel
from project.api.models.farm import FarmModel

class WorkModel(db.Model):
    __tablename__ = 'work'
    id_user = db.Column(db.Integer, db.ForeignKey('_user.id_user'), nullable=False, primary_key=True)
    id_farm = db.Column(db.Integer, db.ForeignKey('farm.id_farm'), nullable=False, primary_key=True)