from flask import Blueprint, request
from flask_restful import Resource, Api
from sqlalchemy import exc

from project import db
from project.api.models.user import UserModel

user_blueprint = Blueprint('_user', __name__)
api = Api(user_blueprint)


@user_blueprint.route('/users/<idUser>', methods=['GET'])
def get_user(idUser):
    """Get single user details"""
    response_object = {
        'status': 'fail',
        'message': 'User does not exist'
    }
    try:
        user = UserModel.query.filter_by(idUser=int(idUser)).first()
        if not user:
            return response_object, 404
        else:
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
    except ValueError:
        return response_object, 404

@user_blueprint.route('/users', methods=['GET'])
def get_all_users():
    """Get all users"""
    response_object = {
        'status': 'success',
        'data': {
            'users': [user.to_json() for user in UserModel.query.all()]
        }
    }
    return response_object, 200