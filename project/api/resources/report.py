from flask import Blueprint, request
from flask_restful import Resource, Api
from sqlalchemy import exc
from project import db
from project.api.models.general_report import GeneralReportModel
from project.api.models.gmd_report import GMDReportModel
from project.api.generator_report.generator_report import ReportGenerator
from flask import Blueprint, request, Response, jsonify, make_response

report_blueprint = Blueprint('ReportModel', __name__)
api = Api(report_blueprint)

import sys

class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'Report!'
        }

@report_blueprint.route('/report/generator_report', methods=['POST'])
def generator_report():
    try:
        report_data = request.get_json()
        generator_report = ReportGenerator()
        generate = generator_report.generate(report_data['user_id'], report_data['type'], report_data['farm_id'])
    except ValueError:
        return jsonify({'error': 'Report not found'}), 400

    return generate, 201

api.add_resource(Ping, '/reports')
