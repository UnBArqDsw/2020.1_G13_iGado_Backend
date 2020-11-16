from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from statistics import median
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
                                is_beef_cattle=bovine_data['is_beef_cattle'],
                                genetical_enhancement=bovine_data['genetical_enhancement'],
                                batch_of_beef=bovine_data['batch_of_beef']);
        else:
            bovine = DairyCattle(farm_id=bovine_data['farm_id'],
                                 name=bovine_data['name'],
                                 breed=bovine_data['breed'],
                                 actual_weight=bovine_data['actual_weight'],
                                 date_of_birth=bovine_data['date_of_birth'],
                                 is_beef_cattle=bovine_data['is_beef_cattle'],
                                 is_pregnant=bovine_data['is_pregnant'],
                                 batch_of_beef=bovine_data['batch_of_beef']);
        db.session.add(bovine)
        db.session.commit()
        return jsonify({'msg': 'Bovine created successfully'}), 201
    except KeyError as error:
        return jsonify({'error': error}), 400
    return Response({'bovine': bovine}, status=200)

@bovine_blueprint.route('/bovine', methods=['GET'])
def bovine():
    try:
        beef_cattles = BeefCattle.query.all()
        dairy_cattles = DairyCattle.query.all()
    except:
        return jsonify({"Error": "Database error"}), 404
    beef_cattles_json = [BeefCattle.to_json(bovine) for bovine in beef_cattles]
    dairy_cattles_json = [DairyCattle.to_json(bovine) for bovine in dairy_cattles]
    return jsonify({'beef_cattles': beef_cattles_json,
                    'dairy_cattles': dairy_cattles_json}), 200

@bovine_blueprint.route('/bovine/<bovine_id>', methods=['GET'])
def get_bovine(bovine_id):
    """Get single bovine details"""
    response_object = {
        'status': 'fail',
        'message': 'Bovine does not exist'
    }
    try:
        beef_cattle = BeefCattle.query.filter_by(bovine_id=int(bovine_id)).first()
        dairy_cattle = DairyCattle.query.filter_by(bovine_id=int(bovine_id)).first()
        if not beef_cattle and not dairy_cattle:
            return response_object, 404
        else:
            if beef_cattle is not None:
                bovine_response = {
                    'data': {
                        'bovine_id': beef_cattle.bovine_id,
                        'farm_id': beef_cattle.farm_id,
                        'name': beef_cattle.name,
                        'date_of_birth': str(beef_cattle.date_of_birth),
                        'breed': beef_cattle.breed,
                        'actual_weight': float(beef_cattle.actual_weight),
                        'is_beef_cattle': beef_cattle.is_beef_cattle,
                        'genetical_enhancement': beef_cattle.genetical_enhancement,
                        'batch_of_beef': beef_cattle.batch_of_beef
                    }
                }
            else:
                bovine_response = {
                    'data': {
                        'bovine_id': dairy_cattle.bovine_id,
                        'farm_id': dairy_cattle.farm_id,
                        'name': dairy_cattle.name,
                        'date_of_birth': str(dairy_cattle.date_of_birth),
                        'breed': dairy_cattle.breed,
                        'actual_weight': float(dairy_cattle.actual_weight),
                        'is_beef_cattle': dairy_cattle.is_beef_cattle,
                        'is_pregnant': dairy_cattle.is_pregnant,
                        'batch_of_beef': dairy_cattle.batch_of_beef
                    }
                }
        return bovine_response, 200
    except ValueError:
        return response_object, 404


@bovine_blueprint.route('/bovine_by_batch/<batch_number>', methods=['GET'])
def get_bovine_by_batch(batch_number):
    try:
        beef_cattle = BeefCattle.query.filter_by(batch_of_beef=int(batch_number)).all()
        dairy_cattle = DairyCattle.query.filter_by(batch_of_beef=int(batch_number)).all()
    except:
        return jsonify({"Error": "Database error"}), 404
    beef_cattles_json = [BeefCattle.to_json(bovine) for bovine in beef_cattle if bovine is not None]
    dairy_cattles_json = [DairyCattle.to_json(bovine) for bovine in dairy_cattle if bovine is not None]
    return jsonify({'beef_cattles': beef_cattles_json,
                    'dairy_cattles': dairy_cattles_json}), 200



@bovine_blueprint.route('/weight_mean_by_batch/<batch_number>', methods=['GET'])
def get_weights_mean_by_batch(batch_number):
    try:
        beef_cattle = BeefCattle.query.filter_by(batch_of_beef=int(batch_number)).all()
        dairy_cattle = DairyCattle.query.filter_by(batch_of_beef=int(batch_number)).all()
    except:
        return jsonify({"Error": "Database error"}), 404
    beef_cattles_json = [BeefCattle.to_json(bovine)['actual_weight'] for bovine in beef_cattle if bovine is not None]
    dairy_cattles_json = [DairyCattle.to_json(bovine)['actual_weight'] for bovine in dairy_cattle if bovine is not None]

    all_bovines_weight_mean = (sum(beef_cattles_json) + sum(dairy_cattles_json)) / (len(beef_cattles_json) + len(dairy_cattles_json)) if (len(beef_cattles_json) + len(dairy_cattles_json)) > 0 else 0
    beef_cattles_weight_mean = (sum(beef_cattles_json) / len(beef_cattles_json)) if len(beef_cattles_json) > 0 else 0
    dairy_cattles_weight_mean = (sum(dairy_cattles_json) / len(dairy_cattles_json)) if len(dairy_cattles_json) > 0 else 0



    return jsonify({'all_bovines_weight_mean': all_bovines_weight_mean if all_bovines_weight_mean > 0 else "This batch has no bovines",
                    'beef_cattles_weight_mean': beef_cattles_weight_mean if beef_cattles_weight_mean > 0 else "This batch has no beef_cattles",
                    'dairy_cattles_weight_mean': dairy_cattles_weight_mean if dairy_cattles_weight_mean > 0 else "This batch has no dairy_cattles" }), 200


@bovine_blueprint.route('/bovine/<bovine_id>', methods=['PATCH'])
def update_bovine(bovine_id):
    response_object = {
        'status': 'fail',
        'message': 'Bovine does not exist'
    }
    try:
        bovine_data = request.get_json()
        if bovine_data['is_beef_cattle']:
            beef_cattle = db.session.query(BeefCattle).filter_by(bovine_id=int(bovine_id)).first()
            if not beef_cattle:
                return response_object, 404
            else:
                beef_cattle.name = bovine_data['name']
                beef_cattle.genetical_enhancement = bovine_data['genetical_enhancement']
                beef_cattle.breed = bovine_data['breed']
                beef_cattle.actual_weight = bovine_data['actual_weight']
                beef_cattle.date_of_birth = bovine_data['date_of_birth']
                db.session.add(beef_cattle)
                db.session.commit()        
                response_object = beef_cattle.to_json()
                return response_object, 200
        else:
            dairy_cattle = db.session.query(DairyCattle).filter_by(bovine_id=int(bovine_id)).first()
            if not dairy_cattle:
                return response_object, 404
            else:
                dairy_cattle.name = bovine_data['name']
                dairy_cattle.is_pregnant = bovine_data['is_pregnant']
                dairy_cattle.breed = bovine_data['breed']
                dairy_cattle.actual_weight = float(bovine_data['actual_weight'])
                dairy_cattle.date_of_birth = bovine_data['date_of_birth']
                db.session.add(dairy_cattle)
                db.session.commit()        
                response_object = dairy_cattle.to_json()
                return response_object, 200
    except ValueError:
        return response_object, 404


@bovine_blueprint.route('/bovine/delete/<bovine_id>', methods=['DELETE'])
def delete_bovine(bovine_id):
    try:
        beef_cattle = db.session.query(BeefCattle).filter_by(bovine_id=int(bovine_id)).first()
    except ValueError:
        return "Bovine do not exists", 404
    if beef_cattle is not None:
        try:
            db.session.query(BeefCattle).filter_by(bovine_id=int(bovine_id)).delete()
            db.session.commit()
            return "Bovine deleted successfully!", 200
        except ValueError:
            return "Cannot delete bovine", 404

    else:
        try:
            db.session.query(DairyCattle).filter_by(bovine_id=int(bovine_id)).delete()
            db.session.commit()
            return "Bovine deleted successfully!", 200
        except ValueError:
            return "Cannot delete bovine", 404
