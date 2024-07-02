from google.cloud import compute_v1

def get_gcp_resources():
    client = compute_v1.InstancesClient()
    project = 'your-project-id'
    zone = 'us-central1-a'
    instances = client.list(project=project, zone=zone)
    return instances