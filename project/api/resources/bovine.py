from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from project import db
from project.api.models.beef_cattle import BeefCattle
from project.api.models.dairy_cattle import DairyCattle
from project.api.models.bovine import Bovine
from project.api.models.farm import FarmModel
from flask_jwt_extended import jwt_required
import json

bovine_blueprint = Blueprint('bovine', __name__)
api = Api(bovine_blueprint)


class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'Bovine!'
        }


api.add_resource(Ping, '/ping')

@bovine_blueprint.route('/bovine', methods=['POST'])
def create_bovine():
    bovine_data = request.get_json()    
    try:
        if bovine_data['is_beef_cattle']:
            bovine = BeefCattle(farm_id=bovine_data['farm_id'],
                                name=bovine_data['name'],
                                date_of_birth=bovine_data['date_of_birth'],
                                breed=bovine_data['breed'],
                                actual_weight=bovine_data['actual_weight'],
                                date_actual_weight=bovine_data['date_actual_weight'],
                                last_weight=bovine_data['last_weight'],
                                date_last_weight=bovine_data['date_last_weight'],
                                is_beef_cattle=bovine_data['is_beef_cattle'],
                                genetical_enhancement=bovine_data['genetical_enhancement']);
        else:
            bovine = DairyCattle(farm_id=bovine_data['farm_id'],
                                 name=bovine_data['name'],
                                 date_of_birth=bovine_data['date_of_birth'],
                                 breed=bovine_data['breed'],
                                 actual_weight=bovine_data['actual_weight'],
                                 date_actual_weight=bovine_data['date_actual_weight'],
                                 last_weight=bovine_data['last_weight'],
                                 date_last_weight=bovine_data['date_last_weight'],
                                 is_beef_cattle=bovine_data['is_beef_cattle'],
                                 is_pregnant=bovine_data['is_pregnant']);
        db.session.add(bovine)
        db.session.commit()
        return jsonify({'msg': 'Bovine created successfully'}), 201
    except KeyError as error:
        return jsonify({'error': error}), 400
    return Response({'bovine': bovine}, status=200)

# @bovine_blueprint.route('/bovine', methods=['GET'])
# def bovine():
#     try:
#         beef_cattles = BeefCattle.query.all()
#         dairy_cattles = DairyCattle.query.all()
#     except:
#         return jsonify({"Error": "Database error"}), 404
#     beef_cattle_json = [BeefCattle.to_json(bovine) for bovine in beef_cattles]
#     dairy_cattle_json = [DairyCattle.to_json(bovine) for bovine in dairy_cattles]
#     return jsonify({'beef_cattles': beef_cattle_json,
#                     'dairy_cattles': dairy_cattle_json}), 200

@bovine_blueprint.route('/bovine/<bovine_id>', methods=['GET'])
def get_bovine(bovine_id):
    """Get single bovine details"""
    response_object = {
        'status': 'fail',
        'message': 'Bovine does not exist'
    }
    try:
        bovine = Bovine.query.filter_by(bovine_id=int(bovine_id)).first()
        if not bovine:
            return response_object, 404
        else:
            response_object = {
                'bovine_id': bovine.bovine_id,
                'farm_id': bovine.farm_id,
                'name': bovine.name,
                'date_of_birth': str(bovine.date_of_birth),
                'breed': bovine.breed,
                'actual_weight': float(bovine.actual_weight),
                'last_weight': float(bovine.last_weight),
                'date_last_weight': str(bovine.date_last_weight),
                'date_actual_weight': str(bovine.date_actual_weight),
                'is_beef_cattle': bovine.is_beef_cattle
            }
        return response_object, 200
    except ValueError:
        return response_object, 404