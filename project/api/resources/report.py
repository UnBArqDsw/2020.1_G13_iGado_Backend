from flask import Blueprint, request, send_file, make_response
from flask_restful import Resource, Api
from sqlalchemy import exc
from project import db
from project.api.models.general_report import GeneralReportModel
from project.api.models.gmd_report import GMDReportModel
from project.api.factories.report_generator import ReportGenerator
from flask import Blueprint, request, Response, jsonify, make_response

from project.api.models.farm import FarmModel
from project.api.models.beef_cattle import BeefCattle
from project.api.models.dairy_cattle import DairyCattle
from project.api.models.bovine import Bovine
import flask_excel as excel
import pyexcel as p

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

@report_blueprint.route('/general_report/<farm_id>', methods=['GET'])
def report_generator(farm_id):
    try:
        farm_info = FarmModel.query.filter_by(farm_id=farm_id).first()
    except:
        return jsonify({"error": "Database error"}), 404
    try:
        beef_cattle = BeefCattle.query.filter_by(farm_id=int(farm_id)).all()
        dairy_cattle = DairyCattle.query.filter_by(farm_id=int(farm_id)).all()
    except:
        return jsonify({"error": "Database error"}), 404
    beef_cattles_json = [BeefCattle.to_json(bovine) for bovine in beef_cattle if bovine is not None]
    dairy_cattles_json = [DairyCattle.to_json(bovine) for bovine in dairy_cattle if bovine is not None]
    # farm_json = FarmModel.to_json(farm_info)

    bovines = dairy_cattles_json
    [bovines.append(beef_cattle) for beef_cattle in beef_cattles_json]
    column_names = ["name", "is_pregnant", "is_beef_cattle", 
                    "farm_id", "date_of_birth", "breed",
                    "bovine_id", "batch_of_beef",
                    "actual_weight"]

    # file = db.session.query(FarmModel.farm_id.label('farm_id'), BeefCattle.bovine_id.label('bovine_id'), BeefCattle.name.label('name'),
    #                         BeefCattle.breed.label('breed'), BeefCattle.actual_weight.label('actual_weight'),
    #                         BeefCattle.is_beef_cattle.label('is_beef_cattle'), BeefCattle.genetical_enhancement.label('genetical_enhancement')
    #                         ).filter(FarmModel.farm_id == farm_id, BeefCattle.farm_id == farm_id).all()
    beef_cattles = BeefCattle.query.filter(BeefCattle.farm_id == farm_id).all()
    dairy_cattles = DairyCattle.query.filter(DairyCattle.farm_id == farm_id).all()

    # import sys
    # print(BeefCattle, file=sys.stderr)
    # print(beef_cattles, file=sys.stderr)
    beef_cattles_values = [BeefCattle.to_json(bovine) for bovine in beef_cattles]
    # beef_cattles_keys = list(beef_cattles[0].to_json().keys())
    # beef_cattles_values.insert(0, beef_cattles_keys)
    dairy_cattles_values = [list(DairyCattle.to_json(bovine).values()) for bovine in dairy_cattles]
    dairy_cattles_keys = list(dairy_cattles[0].to_json().keys())
    dairy_cattles_values.insert(0, dairy_cattles_keys)

    # return excel.make_response_from_tables(
    #         db.session,
    #         [beef_cattles_sheet],
    #         file_type='xlsx',
    #         file_name='general_report'
    #     ), 200

    # file = db.session.query(FarmModel, Bovine).filter(FarmModel.farm_id == farm_id)
    
    # # column_names_2 = ['farm_id', 'bovine_id', 'name', 'breed', 'actual_weight', 'is_beef_cattle', 'genetical_enhancement']

    sheet = {
        'Beef Cattles': beef_cattles_values,
        'Dairy Cattles': dairy_cattles_values,
    }
    import sys
    print(beef_cattles_values, file=sys.stderr)
    beef = p.get_sheet(records=beef_cattles_values)
    # dairy = p.get_sheet(records=dairy_cattles_values)
    # jua = p.get_book(bookdict=sheet)
    # file = p.save_book_as( 
    #     bookdict=sheet,
    #     dest_file_name='general_report.xlsx'
    # )

    file = p.Sheet(beef)
    output = make_response(file.xlsx)
    output.headers["Content-Disposition"] = "attachment; filename=export.xlsx"
    output.headers["Content-type"] = "text/xlsx"
    return output
