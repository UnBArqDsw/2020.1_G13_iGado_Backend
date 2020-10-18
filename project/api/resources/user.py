from flask import Blueprint, request, Response, jsonify
from flask_restful import Resource, Api
from sqlalchemy import exc
from project import db, bcrypt
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
    try:
        user_data = request.get_json()
        user = UserModel(email=user_data['email'],
                         fullname=user_data['fullname'],
                         password=user_data['password'],
                         isproprietary=user_data['isproprietary'])
        db.session.add(user)
        db.session.commit()
        return jsonify({"msg": "User created successfully"}), 201
    except KeyError as error:
        return jsonify({"error": "Missing parameter" + error}), 400
