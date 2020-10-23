from flask import Blueprint, request, Response, jsonify, make_response
from flask_restful import Resource, Api
from sqlalchemy import exc
from project import db, bcrypt
from project.api.models.bovine import BovineModel
import datetime
from flask_jwt_extended import jwt_required

bovine_blueprint = Blueprint('bovine', __name__)
api = Api(bovine_blueprint)


@bovine_blueprint.route('/bovine', methods=['POST'])
@jwt_required
def create_bovine():
    bovine_data = request.get_json()

    bovine = BovineModel(farm_id=bovine_data['farm_id'],
                         breed=bovine_data['breed'],
                         actual_weight=bovine_data['actual_weight'],
                         date_actual_weight=bovine_data['date_actual_weight'],
                         last_weight=bovine_data['last_weight'] if len(bovine_data['last_weight']) > 1 else None,
                         date_last_weight=bovine_data['date_last_weight'] if len(bovine_data['date_last_weight']) >1 else None,
                         date_of_birth=bovine_data['date_of_birth'],
                         is_beef_cattle=bovine_data['is_beef_cattle'])
    try:
        db.session.add(bovine)
        db.session.commit()
    except:
        return jsonify(
            {"erro": "DB error, was not possible not save the bovine"}), 404
 
    return jsonify({"message": "Bovine created successfully!"}), 200


@bovine_blueprint.route('/bovine', methods=['GET'])
@jwt_required
def get_bovines():
    try:
        bovines = BovineModel.query.all()
    except:
        return jsonify({"erro": "Database error"}), 404
    bovine_json = [BovineModel.to_json(bovine) for bovine in bovines]
    return jsonify(bovine_json), 200
