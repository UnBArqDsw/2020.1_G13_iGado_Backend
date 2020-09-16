import os
from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

# instantiate the app
app = Flask(__name__)

api = Api(app)

# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)  

# instantiate the db
db = SQLAlchemy(app)


class Ping(Resource):
    def get(self):
        return {
        'status': 'success',
        'message': 'pong!'
    }

api.add_resource(Ping, '/ping')