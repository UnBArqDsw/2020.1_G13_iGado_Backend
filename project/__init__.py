import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager



# instantiate the db
db = SQLAlchemy()
bcrypt = Bcrypt()


def create_app(script_info=None):

    # instantiate the app
    app = Flask(__name__)
    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)
    app.config['SECRET_KEY'] = 'temporarioMUDARDEPOIS'
    jwt = JWTManager(app)

    # set up extensions
    db.init_app(app)

    # set bcrypt
    bcrypt.init_app(app)

    # register blueprints
    from project.api.resources.example import example_blueprint
    app.register_blueprint(example_blueprint)

    from project.api.resources.user import user_blueprint
    app.register_blueprint(user_blueprint)

    from project.api.resources.farm import farm_blueprint
    app.register_blueprint(farm_blueprint)

    from project.api.resources.work import work_blueprint
    app.register_blueprint(work_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
