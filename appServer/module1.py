from flask import Blueprint, make_response, jsonify
from flask import current_app as app

import logging

bp = Blueprint('module1', __name__, url_prefix='/module1')


@bp.before_request
def before_anything():
    print("before anything in module1..")
    pass


@bp.route('/helloworld', methods=['GET', 'POST'])
def helloworld():
    #Access app config
    print(str(app.config["SOME_PARAMETER"]))
    logging.info('GET /module2/helloworld')
    return make_response(
        jsonify({'message': 'HelloWorld from module1'}),
        200
    )

@bp.app_errorhandler(404)
def not_found(err):
    """Page not found."""
    return make_response(
        jsonify({'message': '404'}),
        404
    )
