import boto3
from flask import Flask, jsonify
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

def get_aws_resources():
    try:
        session = boto3.Session(
            aws_access_key_id='AKIAREHR4UICBFSCZN4M',
            aws_secret_access_key='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',
            region_name='ap-south-1'
        )
        ec2 = session.resource('ec2')
        instances = ec2.instances.all()
        
        resources = []
        for instance in instances:
            instance_name = 'N/A'
            for tag in instance.tags or []:
                if tag['Key'] == 'Name':
                    instance_name = tag['Value']
                    break
            resources.append({'Instance ID': instance.id, 'Instance Name': instance_name})
        
        return resources
    except Exception as e:
        logging.error(f"Error fetching AWS resources: {e}")
        return str(e)
