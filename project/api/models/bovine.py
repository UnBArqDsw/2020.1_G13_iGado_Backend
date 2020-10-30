from project import db
import abc
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.sql import func
from project.api.models.farm import FarmModel


class Bovine(db.Model):
    bovine_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(150), nullable=True)
    date_of_birth = db.Column(db.Date(), nullable=False)
    breed = db.Column(db.String(25), nullable=True)
    actual_weight = db.Column(db.Numeric(5, 2), nullable=False)
    date_actual_weight = db.Column(db.Date(), nullable=False)
    last_weight = db.Column(db.Numeric(5, 2), nullable=True)
    date_last_weight = db.Column(db.Date(), nullable=True)
    is_beef_cattle = db.Column(db.Boolean(), nullable=True)
    farm_id = db.Column(db.Integer, db.ForeignKey('farm.farm_id'))

    __mapper_args__ = {
        'polymorphic_identity': 'bovine'

    }

    def init(self, farm_id, name, date_of_birth, breed, actual_weight, date_actual_weight, last_weight, date_last_weight, is_beef_cattle):
        self.farm_id = farm_id
        self.name = name
        self.breed = breed
        self.actual_weight = actual_weight
        self.date_actual_weight = date_actual_weight
        self.last_weight = last_weight
        self.date_last_weight = date_last_weight
        self.date_of_birth = date_of_birth
        self.is_beef_cattle = is_beef_cattle

    def to_json(self):
        return {
            'bovine_id': self.bovine_id,
            'farm_id': self.farm_id,
            'breed': self.breed,
            'actual_weight': float(self.actual_weight),
            'last_weight': float(self.last_weight),
            'date_last_weight': str(self.date_last_weight),
            'date_actual_weight': str(self.date_actual_weight),
            'date_of_birth': str(self.date_of_birth),
            'is_beef_cattle': self.is_beef_cattle
        }
