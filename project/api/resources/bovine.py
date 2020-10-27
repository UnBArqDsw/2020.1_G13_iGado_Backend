from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from project import db
from project.api.models.beef_cattle import BeefCattle
from project.api.models.dairy_cattle import DairyCattle
from flask_jwt_extended import jwt_required

bovine_blueprint = Blueprint('bovine', __name__)
api = Api(bovine_blueprint)


class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'Report!'
        }


api.add_resource(Ping, '/reports')
