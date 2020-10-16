from flask import Blueprint, request
from flask_restful import Resource, Api
from sqlalchemy import exc

from project import db
from project.api.models.user import UserModel

user_blueprint = Blueprint('_user', __name__)
api = Api(user_blueprint)


class UserResource(Resource):
    def get(self, idUser):
        """Get single User details"""
        user = UserModel.query.filter_by(idUser=idUser).first()
        response_object = {
            'status': 'success',
            'data': {
                'idUser': user.idUser,
                'fullname': user.fullname,
                'email': user.email,
                'password': user.password,
                'isProprietary': user.isProprietary
            }
        }
        return response_object, 200

api.add_resource(UserResource, '/users/<idUser>')