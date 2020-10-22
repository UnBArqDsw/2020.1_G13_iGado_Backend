from project import db
from sqlalchemy import DateTime
from datetime import datetime
import sys

import abc
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.ext.declarative import AbstractConcreteBase

from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.ext.declarative import declared_attr

from project.api.models.user import UserModel
from project.api.models.farm import FarmModel
from sqlalchemy.sql import func


class ReportAbstract(db.Model):
    __abstract__ = True
    __metaclass__ = abc.ABCMeta

    report_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_and_hour_of_emission = db.Column(db.DateTime(timezone=True), default=datetime.utcnow, nullable=False)
    description_report = db.Column(db.Text(convert_unicode=True))

    @declared_attr
    def farm_id(cls): 
        return db.Column(db.Integer, db.ForeignKey('farm.farm_id'))

    def __init__(self, farm_id):
        self.farm_id = farm_id

    def CONST_TEMPLATE_METHOD(self, user_id):
        self.generateHeader(user_id)
        self.generateFarmInfo()
        self.generateMetric()
        self.generateGraphic()
    
    def generate_header(self, user_id):
        months = {
            'January': 'Janeiro',
            'February': 'Fevereiro',
            'March': 'Março',
            'April': 'Abril',
            'May': 'Maio',
            'June': 'Junho',
            'July': 'Julho',
            'August': 'Agosto',
            'September': 'Setembro',
            'October': 'Outubro',
            'November': 'Novembro',
            'December': 'Dezembro'
        }
        now = datetime.now()
        current_time = now.strftime('%d/%m/%y')
        user = UserModel.query.filter_by(user_id=int(user_id)).first()
        farm = FarmModel.query.filter_by(farm_id=int(self.farm_id)).first()

        title = 'Relatório da fazenda ' + farm.farm_name + ' ' + current_time
        creation_date = '{} de {} de {}'.format(now.strftime('%d'), months[now.strftime('%B')], now.strftime('%Y'))
        creation_hour = now.strftime('%H:%M')
        
        return {
            'title': title,
            'creation_date': creation_date,
            'creation_hour': creation_hour,
            'created_by': user.fullname,
            'refers_to': farm.farm_name,
        }
    
    def generate_farm_info(self):
        pass
        # farm = FarmModel.query.filter_by(farm_id=int(self.farm_id)).first()
        # pregnant_dairy_cattle_quantity, dairy_cattle_quantity = 0, 0
        # beef_cattle_quantity = len(farm.beef_cattles)

        # employee_quantity = 0
        # for user in farm.users:
        #     if not user.is_proprietary:
        #         employee_quantity += 1
        
        # for dairy_cattle in farm.dairy_cattles:
        #     if dairy_cattle.pregnant:
        #         pregnant_dairy_cattle_quantity += 1
        #     dairy_cattle_quantity += 1
        # return {
        #     'dairy_cattle_quantity': dairy_cattle_quantity,
        #     'pregnant_dairy_cattle_quantity': pregnant_dairy_cattle_quantity,
        #     'beef_cattle_quantity': beef_cattle_quantity,
        #     'employee_quantity': employee_quantity
        # }


    @abc.abstractmethod
    def generate_metric(self):
        pass

    @abc.abstractmethod
    def generate_graphic(self):
        pass


class ReportModel(ReportAbstract):
    __tablename__ = 'report'

    __mapper_args__ = {
        'polymorphic_identity': 'report'
    }

    def __init__(self, farm_id):
        self.farm_id = farm_id
    

# class ReportIABCZ(ReportModel):
#     def generate_metric(self):
#         pass
#     def generate_graphic(self):
#         pass