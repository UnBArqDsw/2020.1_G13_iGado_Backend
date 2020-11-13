from flask import Blueprint, request, Response, jsonify, make_response
from flask_restful import Resource, Api
from project import db
from project.api.models.weighing_management import WeighingManagementModel
from project.api.models.beef_cattle import BeefCattle
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
