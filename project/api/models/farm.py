from sqlalchemy.sql import func

from project import db
# from project.api.models.work import WorkTable

class FarmModel(db.Model):
    __tablename__ = 'farm'
    idFarm = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sizeFarm = db.Column(db.Integer, nullable=False)
    # users = db.relationship('UserModel', secondary='WorkTable', lazy='subquery', backref=db.backref('farm', lazy=True))

    def __init__(self, sizeFarm):
        self.sizeFarm = sizeFarm
