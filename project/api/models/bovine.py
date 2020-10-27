from project import db
import abc
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta

from sqlalchemy.ext.declarative import declared_attr

from sqlalchemy.sql import func


class BovineAbstract(db.Model):
    __abstract__ = True
    __metaclass__ = abc.ABCMeta

    bovine_id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(150), nullable=True)
    date_of_birth = db.Column(db.Date(), nullable=False)
    breed = db.Column(db.String(25), nullable=True)
    actual_weight = db.Column(db.Numeric(5, 2), nullable=False)
    date_actual_weight = db.Column(db.Date(), nullable=False)
    last_weight = db.Column(db.Numeric(5, 2), nullable=True)
    date_last_weight = db.Column(db.Date(), nullable=True)

    is_beef_cattle = db.Column(db.Boolean(), nullable=False)

    @declared_attr
    def farm_id(cls): 
        return db.Column(db.Integer, db.ForeignKey('farm.farm_id'))

    def __init__(self, farm_id):
        self.farm_id = farm_id
