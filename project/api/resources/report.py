from flask import Blueprint, request
from flask_restful import Resource, Api
from sqlalchemy import exc

from project import db
from project.api.models.report import ReportModel

report_blueprint = Blueprint('ReportModel', __name__)
api = Api(report_blueprint)


class Ping(Resource):
    def get(self):
        report = ReportModel(1)
        report.printHelloWorld()
        db.session.add(report)
        db.session.commit()
        return {
        'status': 'success',
        'message': 'Report!'
    }

api.add_resource(Ping, '/reports')