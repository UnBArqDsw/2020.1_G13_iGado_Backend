from flask import Blueprint, request
from flask_restful import Resource, Api
from sqlalchemy import exc

from project import db
from project.api.models.report import GeneralReportModel
from project.api.models.report import ReportGMDModel
from project.api.generator_report.generator_report import ReportGenerator

report_blueprint = Blueprint('ReportModel', __name__)
api = Api(report_blueprint)

import sys

class Ping(Resource):
    def get(self):
        report = ReportGMDModel(2)
        print(report.CONST_TEMPLATE_METHOD(2), file=sys.stderr)
        db.session.add(report)
        db.session.commit()
        report = GeneralReportModel(1)
        print(report.CONST_TEMPLATE_METHOD(1), file=sys.stderr)
        db.session.add(report)
        db.session.commit()
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
        return generate, 201
    except KeyError:
        return jsonify({'error': 'Missing parameter'}), 400

    return Response({'user': user}, status=200)

api.add_resource(Ping, '/reports')
