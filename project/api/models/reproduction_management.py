from project import db
from datetime import datetime

class ReproductionManagementModel(db.Model):
    __tablename__ = 'reproduction_management'
    reproduction_management_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_and_hour_of_management = db.Column(db.DateTime(timezone=True), nullable=False)
    bovine_id = db.Column(db.Integer, db.ForeignKey('dairy_cattle.bovine_id'))
    bull_breed = db.Column(db.String, default="", nullable=False)
    reproduction_type = db.Column(db.String, default="natural_mount", nullable=False)
    # if reproduction type == insemination
    insemination_amount = db.Column(db.Integer, default=0, nullable=True, )
    insemination_period = db.Column('period_array', db.ARRAY(db.String), nullable=True)
    is_finished = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self, bovine_id, bull_breed, reproduction_type):
        self.date_and_hour_of_management = datetime.utcnow()
        self.bovine_id = bovine_id
        self.bull_breed = bull_breed
        self.reproduction_type = reproduction_type

    def to_json(self):
        reproduction_management = {
            'reproduction_management_id': self.reproduction_management_id,
            'date_and_hour_of_management': self.date_and_hour_of_management,
            'reproduction_type': self.reproduction_type,
            'bovine_id': self.bovine_id,
            'bull_breed': self.bull_breed,
            'is_finished': self.is_finished
        }
        if self.reproduction_type == 'insemination':
            reproduction_management['insemination_amount'] = self.insemination_amount
            reproduction_management['insemination_period'] = self.insemination_period
        return reproduction_management