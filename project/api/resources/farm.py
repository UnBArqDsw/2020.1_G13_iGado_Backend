from flask import Blueprint
from flask_restful import Resource, Api

farm_blueprint = Blueprint('FarmModel', __name__)
api = Api(farm_blueprint)


class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'Farm!'
        }


api.add_resource(Ping, '/farms')
