from flask import jsonify
from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient

def get_azure_resources():
    # Initialize Azure CLI credential
    credential = AzureCliCredential()

    # Replace <subscription_id> with your Azure subscription ID
    subscription_id = '<your_subscription_id>'

    # Initialize ResourceManagementClient with Azure CLI credential
    client = ResourceManagementClient(credential, subscription_id)

    try:
        # Retrieve resources (example: list all resources)
        resources = client.resources.list()
        resource_list = [resource.id for resource in resources]
        return jsonify(resource_list)
    
    except Exception as e:
        return jsonify({'error': str(e)})
