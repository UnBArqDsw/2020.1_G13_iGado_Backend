from flask import Blueprint, request
from flask_restful import Resource, Api
from sqlalchemy import exc

from project import db
from project.api.models.work import WorkModel

work_blueprint = Blueprint('work', __name__)
api = Api(work_blueprint)


class Ping(Resource):
    def get(self):
        return {
        'status': 'success',
        'message': 'pong!'
    }

api.add_resource(Ping, '/ping')