from project.api.models.bovine import Bovine
from project import db


class DairyCattle(Bovine):
    is_pregnant = db.Column(db.Boolean(), nullable=True)
    __mapper_args__ = {
        'polymorphic_identity': 'dairy_cattle'
    }

    def init(self, farm_id, name, date_of_birth, breed, actual_weight,
             date_actual_weight, last_weight, date_last_weight, 
             is_beef_cattle):
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
            'name': self.name,
            'date_of_birth': str(self.date_of_birth),
            'breed': self.breed,
            'actual_weight': float(self.actual_weight),
            'last_weight': float(self.last_weight),
            'date_last_weight': str(self.date_last_weight),
            'date_actual_weight': str(self.date_actual_weight),
            'is_beef_cattle': self.is_beef_cattle,
        }