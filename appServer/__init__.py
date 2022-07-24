import logging
import os

from flask import Flask

from .extensions import db, migrate
from .routes.api import api_bp
from .routes.main import main_bp
from .routes.module2 import bp as module2bp
from appServer import module1


def create_app(app_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SECRET_KEY='dev')

    if app_config is None:
        # load the instance config, if it exists, when not testing
        print(app.config.from_pyfile('app_settings.py', silent=True))
        # app.config.from_mapping({"SQLALCHEMY_DATABASE_URI":"postgresql://cvxuigev:XCl4qDdjdgDmNoIpnomDsltOTegVyKSu@host=ruby.db.elephantsql.com:5432/cvxuigev",
        #                          "SQLALCHEMY_TRACK_MODIFICATIONS":False})
        #app.config.from_object('app_settings.ProductionConfig')
    else:
        app.config.from_mapping(app_config)
        #app.config.from_object(app_config)

    #example of an app config parameter
    app.config.from_mapping(SOME_PARAMETER="SOME_VALUE")
    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    logging.basicConfig(level=logging.DEBUG,
                        format='%(levelname)1.1s %(asctime)s [%(filename)s:%(lineno)d] %(message)s')
    # apply the blueprints to the app
    #Calling Api.init_app() is not required here because registering the blueprint with the app takes care of setting up the routing for the application.
    #api.add_resource(TodoItem, '/todos/<int:id>')

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(module1.bp)
    app.register_blueprint(module2bp)


    @app.before_request
    def load_user():
        print("before all requests even outside blueprint")
    return app
