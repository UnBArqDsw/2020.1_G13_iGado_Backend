from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from project import db


class FarmModel(db.Model):
    __tablename__ = 'farm'
    farm_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    farm_name = db.Column(db.String(128), nullable=False)
    size_farm = db.Column(db.Integer, nullable=False)
    users = relationship('UserModel', secondary='work')
    generalReports = relationship('GeneralReportModel', backref='farm', lazy=True)
    gmdReports = relationship('ReportGMDModel', backref='farm', lazy=True)
    # beef_cattles = relationship('BeefCattleModel', backref='farm', lazy=True)
    # dairy_cattles = relationship('DairyCattleModel', backref='farm', lazy=True)

    def __init__(self, farm_name, size_farm):
        self.farm_name = farm_name
        self.size_farm = size_farm
