from project.api.models.bovine import BovineAbstract
from project import db


class DairyCattle(BovineAbstract):
    __tablename__ = 'dairy_cattle'
    __mapper_args__ = {
        'polymorphic_identity': 'dairy_cattle'
    }

    is_pregnant = db.Column(db.Boolean(), nullable=False)

    def __init__(self, farm_id):
        self.farm_id = farm_id
