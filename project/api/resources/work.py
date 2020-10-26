from flask import Blueprint
from flask_restful import Resource, Api


work_blueprint = Blueprint('work', __name__)
api = Api(work_blueprint)


class Ping(Resource):
    def get(self):
        return {
        'status': 'success',
        'message': 'Work!'
    }

api.add_resource(Ping, '/works')
