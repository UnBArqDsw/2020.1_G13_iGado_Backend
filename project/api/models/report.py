# from project import db
# from sqlalchemy import DateTime
# import datetime
# from sqlalchemy.ext.declarative import AbstractConcreteBase
# from sqlalchemy.orm import configure_mappers
# import abc
# from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta, declared_attr

# class DeclarativeABCMeta(DeclarativeMeta, abc.ABCMeta):
#     pass

# class ReportModel(db.Model, DeclarativeABCMeta):
#     __tablename__ = 'report'
#     __abstract__ = True
#     report_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     date_and_hour_of_emission = db.Column(db.DateTime, default=datetime.datetime.utcnow, nullable=False)
#     description_report = db.Column(db.Text(length=3000, convert_unicode=True))
#     @declared_attr
#     def farm_id(cls):
#         return db.Column(db.Integer, db.ForeignKey('farm.farm_id'))

#     def __init__(self, date_and_hour_of_emission, farm_id):
#         self.date_and_hour_of_emission = date_and_hour_of_emission
#         self.farm_id = farm_id

#     def CONST_TEMPLATE_METHOD(self, user_id):
#         self.generateHeader(user_id)
#         self.generateFarmInfo()
#         self.generateMetric()
#         self.generateGraphic()
    
#     def generate_header(self, user_id):
#         pass
#     def generate_farm_info(self):
#         pass

#     @abc.abstractmethod
#     def generate_metric(self):
#         pass

#     @abc.abstractmethod
#     def generate_graphic(self):
#         pass

# class ReportIABCZ(ReportModel):
#     def generate_metric(self):
#         pass
#     def generate_graphic(self):
#         pass

# configure_mappers()