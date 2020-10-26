from flask import Blueprint
from flask_restful import Resource, Api


example_blueprint = Blueprint('example', __name__)
api = Api(example_blueprint)


class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!'
        }


api.add_resource(Ping, '/ping')
