from flask import jsonify
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
import logging

#configuring logging
logging.basicConfig(level=logging.DEBUG)

def get_azure_resources():
    credential = AzureCliCredential()

    subscription_id = '2780142e-3e5e-4f38-9b5c-5555e7c5f377'

    client = ResourceManagementClient(credential, subscription_id)

    try:
        resources = client.resources.list()
        resource_list = [resource.id for resource in resources]
        return jsonify(resource_list)

    except Exception as e:
        logging.error(f"Error retrieving Azure resources: {str(e)}")
        return jsonify({'error': str(e)})    