import boto3

def get_aws_resources():
    session = boto3.Session(profile_name='default')
    ec2 = session.resource('ec2')
    instances = ec2.instances.all()
    return instances