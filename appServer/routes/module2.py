from flask import Blueprint
import logging

bp = Blueprint('module2', __name__, url_prefix='/module2')


@bp.route('/helloworld')
def helloworld():
    logging.info('GET /module2/helloworld')
    return 'HelloWorld from module2'
