from project import db
from sqlalchemy import DateTime
import datetime
import sys

import abc
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.ext.declarative import AbstractConcreteBase

from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.ext.declarative import declared_attr


class ReportAbstract(db.Model, metaclass=abc.ABCMeta):
    __abstract__ = True

    def CONST_TEMPLATE_METHOD(self, user_id):
        self.generateHeader(user_id)
        self.generateFarmInfo()
        self.generateMetric()
        self.generateGraphic()
    
    def generate_header(self, user_id):
        pass
    
    def generate_farm_info(self):
        pass

    @abc.abstractmethod
    def generate_metric(self):
        pass

    @abc.abstractmethod
    def generate_graphic(self):
        pass

    def printHelloWorld(self):
        print('Hello World', file=sys.stderr)

class ReportModel(ReportAbstract):
    __tablename__ = 'report'
    report_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_and_hour_of_emission = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    description_report = db.Column(db.Text(convert_unicode=True))

    __mapper_args__ = {
        'polymorphic_identity': 'report'
    }
    # farm_id = db.Column(db.Integer, db.ForeignKey('farm.farm_id'))

    def __init__(self, farm_id):
        self.farm_id = farm_id
    

# class ReportIABCZ(ReportModel):
#     def generate_metric(self):
#         pass
#     def generate_graphic(self):
#         pass