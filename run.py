"""Init script."""
from flask import Flask, Blueprint
from flask_restplus import Api

from bpmninja.bpm import bpm_ns
from bpmninja.db import db, Session

app = Flask(__name__)
app.config['RESTPLUS_VALIDATE'] = True

api = Api(version='1.0',
          title='BPM Ninja API',
          description='A simple flask API to handle the backend of bpmninja'
          )


def initialize_app():
    """Initialize bpmninja API flask app. Register ns (namespaces) and blueprints."""
    api.add_namespace(bpm_ns, path='/bpm')
    bp = Blueprint('api', __name__, url_prefix='/api/v1')
    api.init_app(bp)

    app.register_blueprint(bp)


if __name__ == '__main__':
    initialize_app()
    app.run(host='127.0.0.1', port=5000, debug=True)
