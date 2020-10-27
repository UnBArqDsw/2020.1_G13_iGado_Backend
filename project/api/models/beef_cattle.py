from project.api.models.bovine import BovineAbstract
from project import db


class BeefCattle(BovineAbstract):
    __tablename__ = 'beef_cattle'
    __mapper_args__ = {
        'polymorphic_identity': 'beef_cattle'
    }

    genetical_enhancement = db.Column(db.String(50), nullable=True)

    def __init__(self, farm_id):
        self.farm_id = farm_id
