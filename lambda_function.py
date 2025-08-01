import json
import urllib.parse
import boto3
import time

s3 = boto3.client('s3')
cloudfront = boto3.client('cloudfront')

def lambda_handler(event, context):
    # Get the object from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    
    try:
        # Get the object
        response = s3.get_object(Bucket=bucket, Key=key)
        print(f"CONTENT TYPE: {response['ContentType']}")
        print(f"New file uploaded: s3://{bucket}/{key}")
        
        # Create CloudFront invalidation
        cloudfront.create_invalidation(
            DistributionId='E2DCC90HHAPUFJ',
            InvalidationBatch={
                'Paths': {
                    'Quantity': 1,
                    'Items': ['/' + key]
                },
                'CallerReference': str(int(time.time()))
            }
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps(f'Successfully processed {key}')
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error processing {key}')
        }
