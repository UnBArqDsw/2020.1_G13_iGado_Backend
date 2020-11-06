from flask import Blueprint, request, Response, jsonify, make_response
from flask_restful import Resource, Api
from sqlalchemy import exc, update, table, column
from project import db
from project.api.models.reproduction_management import ReproductionManagementModel

reproduction_management_blueprint = Blueprint('ReproductionManagementModel', __name__)
api = Api(reproduction_management_blueprint)

import sys

@reproduction_management_blueprint.route('/reproduction_management/<bovine_id>', methods=['GET'])
def get_reproduction_management(bovine_id):
    response_object = {
        'status': 'fail',
        'message': 'Reproduction management does not exist'
    }
    try:
        response_object = {
            'status': 'success',
            'data': {
                'reproduction_managements': [reproduction_management.to_json() for 
                    reproduction_management in ReproductionManagementModel.query.filter_by(bovine_id=int(bovine_id)).all()]
            }
        }
        return response_object, 200
    except ValueError:
        return response_object, 404

@reproduction_management_blueprint.route('/reproduction_management', methods=['GET'])
def get_all_reproduction_managements():
    response_object = {
        'status': 'success',
        'data': {
            'reproduction_managements': [reproduction_management.to_json() for 
                reproduction_management in ReproductionManagementModel.query.all()]
        }
    }
    return response_object, 200

@reproduction_management_blueprint.route('/reproduction_management', methods=['POST'])
def perform_management():
    try:
        reproduction_management_data = request.get_json()
        reproduction_management = ReproductionManagementModel(
            bovine_id=reproduction_management_data['bovine_id'],
            bull_breed=reproduction_management_data['bull_breed'],
            reproduction_type=reproduction_management_data['reproduction_type'])
        if 'bull_id' in reproduction_management_data.keys():
            reproduction_management.bull_id = reproduction_management_data['bull_id']
        if reproduction_management_data['reproduction_type'] == "insemination":
            reproduction_management.insemination_period = []
            reproduction_management.insemination_amount = reproduction_management_data['insemination_amount']
            reproduction_management.insemination_period += reproduction_management_data['insemination_period']
        db.session.add(reproduction_management)
        db.session.commit()
        return jsonify({'msg': 'Management performed successfully'}), 201
    except ValueError:
        return jsonify({'error': 'Fail to perform management'}), 400

    return Response({'reproduction_management': reproduction_management}, status=200)

@reproduction_management_blueprint.route('/reproduction_management/<reproduction_management_id>', methods=['PATCH'])
def update_management(reproduction_management_id):
    response_object = {
        'status': 'fail',
        'message': 'Reproduction management does not exist'
    }
    try:
        reproduction_management_data = request.get_json()
        reproduction_management = ReproductionManagementModel.query.filter_by(
            reproduction_management_id=int(reproduction_management_id)).first() # .update({"insemination_period": reproduction_management.insemination_period.append(reproduction_management_data['insemination_period'])}, synchronize_session='evaluate')
        print(type(reproduction_management))
        print(reproduction_management)
        # reproduction_management = table('reproduction_management')
        # stmp = update(reproduction_management).where(reproduction_management.c.reproduction_management_id == reproduction_management_id).values(insemination_period = ["Manhã, Tarde"])
        if not reproduction_management:
            return response_object, 404
        else:
            print("Patch management", file=sys.stderr)
            if len(reproduction_management.insemination_period) < reproduction_management.insemination_amount:
                print("1 if entrou", file=sys.stderr)
                reproduction_management.insemination_period += reproduction_management_data['insemination_period']

            if len(reproduction_management.insemination_period) == reproduction_management.insemination_amount:
                print("2 if entrou", file=sys.stderr)
                reproduction_management.is_finished = True
            
            print("reproduction insemi perd data: ", reproduction_management_data['insemination_period'], file=sys.stderr)
            print("reproduction insemi perd: ", reproduction_management, file=sys.stderr)
        #     # db.session.add(reproduction_management)
        ReproductionManagementModel.query.filter_by(
            reproduction_management_id=int(reproduction_management_id)).update(reproduction_management, synchronize_session='evaluate')
        db.session.commit()
        response_object = reproduction_management.to_json()
        return response_object, 200
    except ValueError:
        return response_object, 404