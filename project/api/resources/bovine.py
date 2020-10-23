from flask import Blueprint, request, jsonify
from flask_restful import Api
from project import db
from project.api.models.bovine import BovineModel
from flask_jwt_extended import jwt_required

bovine_blueprint = Blueprint('bovine', __name__)
api = Api(bovine_blueprint)


@bovine_blueprint.route('/bovine', methods=['POST'])
@jwt_required
def create_bovine():
    bovine_data = request.get_json()

    bovine = BovineModel(farm_id=bovine_data['farm_id'],
                         breed=bovine_data['breed'],
                         weight_=bovine_data['weight_'],
                         date_of_birth=bovine_data['date_of_birth'],
                         is_beef_cattle=bovine_data['is_beef_cattle'])
    try:
        db.session.add(bovine)
        db.session.commit()
    except ValueError:
        return jsonify(
            {"erro": "DB error, was not possible not save the bovine"}), 404

    return jsonify({"message": "Bovine created successfully!"}), 200


@bovine_blueprint.route('/bovine', methods=['GET'])
@jwt_required
def get_bovines():
    try:
        bovines = BovineModel.query.all()
    except Exception:
        return jsonify({"erro": "Database error"}), 404
    bovine_json = [BovineModel.to_json(bovine) for bovine in bovines]
    return jsonify(bovine_json), 200
