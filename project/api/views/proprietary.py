from flask import Blueprint, request
from flask_restful import Resource, Api
from sqlalchemy import exc

from project import db
from project.api.models.proprietary import ProprietaryModel

proprietary_blueprint = Blueprint('proprietary', __name__)
api = Api(proprietary_blueprint)


class ProprietaryResource(Resource):
    def get(self, idProprietary):
        """Get single proprietary details"""
        proprietary = ProprietaryModel.query.filter_by(idProprietary=idProprietary).first()
        response_object = {
            'status': 'success',
            'data': {
                'idProprietary': proprietary.idProprietary,
                'fullname': proprietary.fullname,
                'email': proprietary.email,
                'password': proprietary.password
            }
        }
        return response_object, 200

api.add_resource(ProprietaryResource, '/proprietaries/<idProprietary>')