from project.api.models.bovine import BovineAbstract
from project import db


class DairyCattle(BovineAbstract):
    __tablename__ = 'dairy_cattle'
    __mapper_args__ = {
        'polymorphic_identity': 'dairy_cattle'
    }

    is_pregnant = db.Column(db.Boolean(), nullable=False)

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
