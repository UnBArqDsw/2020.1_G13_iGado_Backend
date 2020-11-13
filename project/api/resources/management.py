from flask import Blueprint, request, Response, jsonify, make_response
from flask_restful import Resource, Api

from project import db
from project.api.models.weighing_management import WeighingManagementModel
from project.api.models.reproduction_management import ReproductionManagementModel
from project.api.factories.management_generator import ManagementGenerator

import sys

management_blueprint = Blueprint('management', __name__)
api = Api(management_blueprint)

@management_blueprint.route('/management', methods=['POST'])
def create_management():
    try:
        management_data = request.get_json()
        management_generator = ManagementGenerator()
        management = management_generator.generate(management_data['type'], management_data)
        return jsonify({'msg': 'Management created successfully'}), 201
    except KeyError:
        return jsonify({'error': 'Missing parameter'}), 400

@management_blueprint.route('/management/<bovine_id>', methods=['GET'])
def get_management(bovine_id):
    response_object = {
        'status': 'fail',
        'message': 'Reproduction management does not exist'
    }
    try:
        response_object = {
            'status': 'success',
            'data': {
                'weighting_managements': [management.to_json() for 
                    management in WeighingManagementModel.query.filter_by(bovine_id=int(bovine_id)).all()],
                'reproduction_managements': [management.to_json() for 
                    management in ReproductionManagementModel.query.filter_by(bovine_id=int(bovine_id)).all()]
            }
        }
        return response_object, 200
    except ValueError:
        return response_object, 404

@management_blueprint.route('/management', methods=['GET'])
def get_all_managements():
    print("Getall")
    response_object = {
        'status': 'success',
        'data': {
            'weighing_managements': [weighing_management.to_json() for 
                weighing_management in WeighingManagementModel.query.all()],
            'reproduction_managements': [reproduction_management.to_json() for 
                reproduction_management in ReproductionManagementModel.query.all()]
        }
    }
    return response_object, 200