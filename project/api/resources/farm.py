from flask import Blueprint, request
from flask_restful import Resource, Api
from sqlalchemy import exc

from project import db
from project.api.models.farm import FarmModel

farm_blueprint = Blueprint('FarmModel', __name__)
api = Api(farm_blueprint)


class Ping(Resource):
    def get(self):
        return {
        'status': 'success',
        'message': 'Farm!'
    }

api.add_resource(Ping, '/farms')