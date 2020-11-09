from project import db
from datetime import datetime

class WeighingManagementModel(db.Model):
    __tablename__ = 'weighing_management'
    weighing_management_id = db.Column(db.Integer, primary_key=True,
                                       autoincrement=True)
    date_and_hour_of_management = db.Column(db.DateTime(timezone=True),
                                            default=datetime.utcnow,
                                            nullable=False)
    date_of_actual_weighing = db.Column(db.DateTime(timezone=True),
                                        nullable=False)
    date_of_old_weighing = db.Column(db.DateTime(timezone=True),
                                     nullable=False)
    old_weight = db.Column(db.Numeric(5, 2), nullable=False)
    actual_weight = db.Column(db.Numeric(5, 2), nullable=False)
    bovine_id = db.Column(db.Integer, db.ForeignKey('beef_cattle.bovine_id'))

    def __init__(self, date_of_actual_weighing, date_of_old_weighing,
                 old_weight, actual_weight, bovine_id):
        self.date_of_old_weighing = date_of_old_weighing
        self.date_of_actual_weighing = date_of_actual_weighing
        self.old_weight = old_weight
        self.actual_weight = actual_weight
        self.bovine_id = bovine_id

    def to_json(self):
        weighing_management = {
            'weighing_management_id': self.weighing_management_id,
            'date_and_hour_of_management': self.date_and_hour_of_management,
            'date_of_old_weighing': self.date_of_old_weighing,
            'date_of_actual_weighing': self.date_of_actual_weighing,
            'bovine_id': self.bovine_id,
            'old_weight': self.old_weight,
        }
        return weighing_management
