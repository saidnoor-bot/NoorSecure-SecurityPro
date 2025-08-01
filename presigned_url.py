import json
import boto3
import uuid
from datetime import datetime

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Get query parameters
    query_params = event.get('queryStringParameters', {}) or {}
    file_name = query_params.get('fileName', '')
    file_type = query_params.get('fileType', '')
    
    if not file_name or not file_type:
        return {
            'statusCode': 400,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({'error': 'fileName and fileType are required'})
        }
    
    # Generate a unique file name
    unique_file_name = f"{datetime.now().strftime('%Y%m%d%H%M%S')}-{uuid.uuid4().hex[:8]}-{file_name}"
    
    # Generate the presigned URL
    presigned_url = s3.generate_presigned_url(
        'put_object',
        Params={
            'Bucket': 'noorshare-secure-uploads-new',
            'Key': unique_file_name,
            'ContentType': file_type
        },
        ExpiresIn=300  # URL expires in 5 minutes
    )
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'uploadURL': presigned_url,
            'fileName': unique_file_name
        })
    }
