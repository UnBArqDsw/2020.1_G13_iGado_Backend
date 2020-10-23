from project import db


class BovineModel(db.Model):
    __tablename__ = 'bovine'
    id_bovine = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    farm_id = db.Column(db.Integer(), db.ForeignKey('farm.farm_id'),
                        nullable=False)
    breed = db.Column(db.String(25), nullable=True)
    weight_ = db.Column(db.Numeric(5, 2), nullable=False)
    date_of_birth = db.Column(db.Date(), nullable=False)
    is_beef_cattle = db.Column(db.Boolean(), nullable=False)

    def __init__(self, farm_id, breed, weight_, date_of_birth, is_beef_cattle):
        self.farm_id = farm_id
        self.breed = breed
        self.weight_ = weight_
        self.date_of_birth = date_of_birth
        self.is_beef_cattle = is_beef_cattle
        
    def to_json(self):
        return {
            'id_bovine': self.id_bovine,
            'farm_id': self.farm_id,
            'breed': self.breed,
            'weight_': float(self.weight_),
            'date_of_birth': str(self.date_of_birth),
            'is_beef_cattle': self.is_beef_cattle
        }