# Import flask dependencies
from flask import Blueprint, request, render_template
from app import app


# # Define the blueprint: 'auth', define app
# app = Blueprint('index', __name__, template_folder='templates')
#
#
# @app.route('/', methods=['GET'])
# def index():
#     return render_template("index.html")


@app.route('/')
@app.route('/index')
def index():
    """Render landing page."""
    return render_template('index.html', title="Landing Page")
