# from sqlalchemy.sql import func
# from sqlalchemy.orm import relationship

# from project import db
# from project.api.models.user import UserModel
# from project.api.models.farm import FarmModel

# class WorkModel(db.Model):
#     __tablename__ = 'work'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     idFarm = db.Column(db.Integer, db.ForeignKey('farm.idFarm'), nullable=False)
#     idUser = db.Column(db.Integer, db.ForeignKey('_user.idUser'), nullable=False)

#     farms = relationship(FarmModel, backref=('work', cascade='all, delete-orphan'))
#     user = relationship(UserModel, backref=('work', cascade='all, delete-orphan'))