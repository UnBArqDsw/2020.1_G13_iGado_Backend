from flask import Blueprint, request, Response, jsonify, make_response
from flask_restful import Resource, Api
from project import db
from project.api.models.weighing_management import WeighingManagementModel
from project.api.models.beef_cattle import BeefCattle
import sys

weighing_management_blueprint = Blueprint('weighing_management', __name__)
api = Api(weighing_management_blueprint)

@weighing_management_blueprint.route('/weighing_management', methods=['POST'])
def create_weighing_management():
    try:
        weighing_management_data = request.get_json()
        beef_cattle = BeefCattle.query.filter_by(bovine_id=int(weighing_management_data['bovine_id'])).first()
        weighing_management = WeighingManagementModel(date_of_old_weighing=beef_cattle.date_of_actual_weighing,
                         date_of_actual_weighing=weighing_management_data['date_of_actual_weighing'],
                         actual_weight=weighing_management_data['actual_weight'],
                         bovine_id=weighing_management_data['bovine_id'],
                         old_weight=beef_cattle.actual_weight)
        db.session.add(weighing_management)
        db.session.commit()
        beef_cattle.actual_weight = weighing_management_data['actual_weight']
        beef_cattle.date_of_actual_weighing = weighing_management_data['date_of_actual_weighing']
        db.session.add(beef_cattle)
        db.session.commit()
    
        return jsonify({'msg': 'Management created successfully'}), 201
    except KeyError:
        return jsonify({'error': 'Missing parameter'}), 400

    return Response({'Management': weighing_management}, status=200)
