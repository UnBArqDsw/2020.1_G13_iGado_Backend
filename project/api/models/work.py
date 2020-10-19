from project import db


class WorkModel(db.Model):
    __tablename__ = 'work'
    user_id = db.Column(db.Integer, db.ForeignKey('_user.user_id'),
                        nullable=False, primary_key=True)
    farm_id = db.Column(db.Integer, db.ForeignKey('farm.farm_id'),
                        nullable=False, primary_key=True)
