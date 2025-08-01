import json
import boto3
import os
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table_name = "UserSessionTable"  # Your actual table name
table = dynamodb.Table(table_name)

def lambda_handler(event, context):
    session_id = str(uuid.uuid4())
    timestamp = datetime.utcnow().isoformat()

    # Example user session data
    session_data = {
        'session_id': session_id,
        'timestamp': timestamp,
        'ip_address': event['requestContext']['identity']['sourceIp'],
        'user_agent': event['headers']['User-Agent']
    }

    # Store session in DynamoDB
    table.put_item(Item=session_data)

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Session stored', 'session_id': session_id})
    }

