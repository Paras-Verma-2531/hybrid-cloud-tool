from flask import Blueprint, render_template, jsonify
from .aws_services import get_aws_resources
from .azure_services import get_azure_resources
#from .gcp_services import get_gcp_resources

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/resources')
def resources():
    return render_template('resources.html')

@main.route('/aws_resources')
def aws_resources():
    resources = get_aws_resources()
    if isinstance(resources, str):  # Check if resources is an error message
        return jsonify({'error': resources}), 500
    return jsonify(resources)

@main.route('/azure_resources')
def azure_resources():
    return get_azure_resources()

# @main.route('/gcp_resources')
# def gcp_resources():
#     resources = get_gcp_resources()
#     return jsonify([instance.name for instance in resources])