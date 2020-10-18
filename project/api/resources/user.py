from flask import Blueprint, request, Response, jsonify, make_response
from flask_restful import Resource, Api
from sqlalchemy import exc
from project import db, bcrypt
from project.api.models.user import UserModel
from flask_jwt_extended import (
    jwt_required, create_access_token,
    get_jwt_identity
)

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
                    'iduser': user.iduser,
                    'fullname': user.fullname,
                    'email': user.email,
                    'password': user.password,
                    'isproprietary': user.isproprietary
                }
            }
            return response_object, 200
    except ValueError:
        return response_object, 404


@user_blueprint.route('/user/create', methods=['POST'])
def create_user():
    user_data = request.get_json()
    user = UserModel(email=user_data['email'], fullname=user_data['fullname'],password=user_data['password'],isProprietary=user_data['isproprietary'])
    db.session.add(user)
    db.session.commit()

    return Response({ "user":user}, status=200)

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


@user_blueprint.route('/user/login', methods=['POST'])
def user_login():
    login_data = request.get_json()

    try:
        user = UserModel.query.filter_by(email=login_data['email']).first()
    except:
        return make_response(jsonify("erro: Db error!"), 404)
    
    if not user:
        return make_response(jsonify("erro2: Db error!"), 404)
    
    import sys

    if login_data['password'] != user.password:
        return make_response(jsonify("erro: Incorrect Password!"), 404)

    access_token = create_access_token(identity=user.email)
    return make_response(jsonify(access_token), 200)

@user_blueprint.route('/user/test_token', methods=['GET'])
@jwt_required
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
