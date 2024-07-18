from flask import Blueprint, render_template, jsonify, request
from .aws_services import get_aws_resources
from .azure_services import get_azure_resources, fetch_metrics
import plotly.express as px
import logging

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
    resources = get_azure_resources()
    return jsonify(resources)

@main.route('/azure_metrics/<resource_name>/<resource_type>')
def azure_metrics(resource_name, resource_type):
    resources_list = get_azure_resources()
    
    # Find the resource with matching name and type
    resource_id = None
    for resource in resources_list:
        if resource['name'] == resource_name and resource['type'] == resource_type:
            resource_id = resource['id']
            break
    
    if not resource_id:
        return jsonify({'error': f'Resource {resource_name} of type {resource_type} not found'}), 404

    timestamps, values = fetch_metrics(resource_id)

    # Plotting all metrics dynamically
    fig = px.line(x=timestamps, y=values, labels={'x': 'Time', 'y': 'Value'})
    graph_html = fig.to_html(full_html=False)
    return render_template('azure_metrics.html', graph_html=graph_html)