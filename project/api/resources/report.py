from flask import Blueprint, request
from flask_restful import Resource, Api
from sqlalchemy import exc

from project import db
from project.api.models.report import GeneralReportModel
from project.api.models.report import ReportGMDModel

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

api.add_resource(Ping, '/reports')