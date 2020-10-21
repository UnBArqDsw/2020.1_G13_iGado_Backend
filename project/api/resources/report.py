# from flask import Blueprint, request
# from flask_restful import Resource, Api
# from sqlalchemy import exc

# from project import db
# from project.api.models.report import ReportIABCZ

# report_blueprint = Blueprint('ReportIABCZ', __name__)
# api = Api(report_blueprint)


# class Ping(Resource):
#     def get(self):
#         return {
#         'status': 'success',
#         'message': 'Report!'
#     }

# api.add_resource(Ping, '/reports')

# @user_blueprint.route('/user/create', methods=['POST'])
# def create_user():
#     try:
#         user_data = request.get_json()
#         user = UserModel(email=user_data['email'],
#                          fullname=user_data['fullname'],
#                          password=user_data['password'],
#                          is_proprietary=user_data['is_proprietary'])
#         db.session.add(user)
#         db.session.commit()
#         if user_data['farm_size']:
#             farm_id = user.create_farm(farm_name=user_data['farm_name'],
#                                        farm_size=user_data['farm_size'])
#         else:
#             farm_id = user_data['farm_id']
#         work = WorkModel(user_id=user.user_id, farm_id=farm_id)
#         db.session.add(work)
#         db.session.commit()
#         return jsonify({'msg': 'User created successfully'}), 201
#     except KeyError:
#         return jsonify({'error': 'Missing parameter'}), 400

#     return Response({'user': user}, status=200)