from sqlalchemy.orm import relationship

from project import db, bcrypt
from project.api.models.farm import FarmModel
from project.api.models.work import WorkModel


class UserModel(db.Model):
    __tablename__ = '_user'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(128), nullable=False)
    fullname = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    is_proprietary = db.Column(db.Boolean, default=False)
    farms = relationship('FarmModel', secondary='work')

    def __init__(self, email, fullname, password, is_proprietary):
        self.email = email
        self.fullname = fullname
        self.password = bcrypt.generate_password_hash(password).decode()
        self.is_proprietary = is_proprietary

    def to_json(self):
        return {
            'user_id': self.user_id,
            'email': self.email,
            'fullname': self.fullname,
            'password': self.password,
            'is_proprietary': self.is_proprietary,
            'farms': [farm.farm_id for farm in self.farms]
        }
