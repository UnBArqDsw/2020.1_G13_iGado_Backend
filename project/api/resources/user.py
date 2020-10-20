from flask import Blueprint, request, Response, jsonify, make_response
from flask_restful import Resource, Api
from sqlalchemy import exc
from project import db, bcrypt
from project.api.models.user import UserModel
from project.api.models.work import WorkModel
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

user_blueprint = Blueprint('_user', __name__)
api = Api(user_blueprint)


@user_blueprint.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    """Get single user details"""
    response_object = {
        'status': 'fail',
        'message': 'User does not exist'
    }
    try:
        user = UserModel.query.filter_by(user_id=int(user_id)).first()
        if not user:
            return response_object, 404
        else:
            response_object = {
                'status': 'success',
                'data': {
                    'user_id': user.user_id,
                    'fullname': user.fullname,
                    'email': user.email,
                    'password': user.password,
                    'is_proprietary': user.is_proprietary,
                    'farms': [farm.farm_id for farm in user.farms]
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
                         is_proprietary=user_data['is_proprietary'])
        db.session.add(user)
        db.session.commit()
        if 'farm_size' in user_data:
            farm_id = user.create_farm(user_data['farm_size'])
        else:
            farm_id = user_data['farm_id']
        work = WorkModel(user_id=user.user_id, farm_id=farm_id)
        db.session.add(work)
        db.session.commit()
        return jsonify({'msg': 'User created successfully'}), 201
    except KeyError:
        return jsonify({'error': 'Missing parameter'}), 400

    return Response({'user': user}, status=200)


@user_blueprint.route('/user', methods=['GET'])
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
    except Exception:
        return make_response(jsonify("Error: Database error!"), 404)

    if not user:
        return make_response(jsonify("Error: User not found!"), 404)

    if login_data['password'] != user.password:
        return make_response(jsonify("Error: Incorrect password!"), 404)

    access_token = create_access_token(identity=user.email)
    return make_response(jsonify(access_token), 200)


@user_blueprint.route('/user/test_token', methods=['GET'])
@jwt_required
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
