from flask import Blueprint, request
from flask_restful import Resource, Api
from sqlalchemy import exc

from project import db
from project.api.models.example import Example

example_blueprint = Blueprint('example', __name__)
api = Api(example_blueprint)


class Ping(Resource):
    def get(self):
        return {
        'status': 'success',
        'message': 'pong!'
    }

api.add_resource(Ping, '/ping')