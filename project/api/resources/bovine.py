from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from project import db
from project.api.models.beef_cattle import BeefCattle
from project.api.models.dairy_cattle import DairyCattle
from project.api.models.bovine import BovineAbstract
from project.api.models.farm import FarmModel
from flask_jwt_extended import jwt_required

bovine_blueprint = Blueprint('bovine', __name__)
api = Api(bovine_blueprint)


class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'Bovine!'
        }


api.add_resource(Ping, '/bovine')

@bovine_blueprint.route('/bovine/create', methods=['POST'])
def create_bovine():
    bovine_data = request.get_json()
    try:
        bovine = BeefCattle(farm_id=bovine_data['farm_id'],
                            name=bovine_data['name'],
                            date_of_birth=bovine_data['date_of_birth'],
                            breed=bovine_data['breed'],
                            actual_weight=bovine_data['actual_weight'],
                            date_actual_weight=bovine_data['date_actual_weight'],
                            last_weight=bovine_data['last_weight'],
                            date_last_weight=bovine_data['date_last_weight'],
                            is_beef_cattle=bovine_data['is_beef_cattle']);
        db.session.add(bovine)
        db.session.commit()
        return jsonify({'msg': 'Bovine created successfully'}), 201
    except KeyError:
        return jsonify({'error': 'Missing parameter'}), 400
    return Response({'bovine': bovine}, status=200)
