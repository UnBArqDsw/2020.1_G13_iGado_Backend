from flask import Blueprint, request, Response
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
        user = UserModel.query.filter_by(iduser=int(idUser)).first()
        if not user:
            return response_object, 404
        else:
            response_object = {
                'status': 'success',
                'data': {
                    'idUser': user.iduser,
                    'fullname': user.fullname,
                    'email': user.email,
                    'password': user.password,
                    'isProprietary': user.isproprietary
                }
            }
            return response_object, 200
    except ValueError:
        return response_object, 404


@user_blueprint.route('/user/create', methods=['POST'])
def create_user():
    import sys
    try:
        user_data = request.get_json()
        print(user_data['isproprietary'], file=sys.stderr)
        user = UserModel(email=user_data['email'], fullname=user_data['fullname'],password=user_data['password'],isProprietary=user_data['isproprietary'])
        db.session.add(user)
        db.session.commit()
        return Response({ "user":user}, status=200)
    except Exception as error:
        print(error)

