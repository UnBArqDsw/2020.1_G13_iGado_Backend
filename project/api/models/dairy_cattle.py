from project.api.models.bovine import Bovine
from project import db


class DairyCattle(Bovine):
    bovine_id = db.Column(db.Integer, db.ForeignKey('bovine.bovine_id'), primary_key=True)
    is_pregnant = db.Column(db.Boolean(), nullable=True)
    reproduction_managements = db.relationship('ReproductionManagementModel', backref='farm', lazy=True)
    __mapper_args__ = {
        'polymorphic_identity': 'dairy_cattle'
    }

    def init(self, farm_id, name, date_of_birth, breed, actual_weight,
             is_beef_cattle, is_pregnant, batch_of_beef):
        self.farm_id = farm_id
        self.name = name
        self.breed = breed
        self.actual_weight = actual_weight
        self.date_of_birth = date_of_birth
        self.is_beef_cattle = is_beef_cattle
        self.is_pregnant = is_pregnant,
        self.batch_of_beef = batch_of_beef

    def to_json(self):
        return {
            'bovine_id': self.bovine_id,
            'farm_id': self.farm_id,
            'name': self.name,
            'date_of_birth': str(self.date_of_birth),
            'breed': self.breed,
            'actual_weight': float(self.actual_weight),
            'is_beef_cattle': self.is_beef_cattle,
            'is_pregnant': self.is_pregnant,
            'batch_of_beef': self.batch_of_beef
        }