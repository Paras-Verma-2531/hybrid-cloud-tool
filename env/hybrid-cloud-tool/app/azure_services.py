from azure.identity import DefaultAzureCredential
from azure.mgmt.monitor import MonitorManagementClient
from azure.mgmt.resource import ResourceManagementClient
from datetime import datetime, timedelta

subscription_id = '2780142e-3e5e-4f38-9b5c-5555e7c5f377'
resource_group_name = 'Project'

def get_azure_resources():
    credential = DefaultAzureCredential()
    client = ResourceManagementClient(credential, subscription_id)
    resources = client.resources.list()
    resources_list = []
    
    for resource in resources:
        resources_list.append({
            'id': resource.id,
            'name': resource.name,
            'type': resource.type,
            'location': resource.location
        })
    
    return resources_list

def fetch_metrics(resource_id):
    credential = DefaultAzureCredential()
    monitor_client = MonitorManagementClient(credential, subscription_id)

    # Define the time range for the metrics (last 24 hours)
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(days=1)

    # List available metrics for the resource
    metrics = monitor_client.metrics.list(
        resource_id,
        timespan="{}/{}".format(start_time, end_time),
        interval='PT1H'
    )

    # Initialize empty lists to store timestamps and values for all metrics
    all_timestamps = []
    all_values = []

    for metric in metrics:
        for time_series in metric.timeseries:
            for data in time_series.data:
                all_timestamps.append(data.time_stamp)
                all_values.append(data.average)

    return all_timestamps, all_values