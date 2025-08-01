import json
import boto3
import urllib.parse

s3 = boto3.client('s3')
rekognition = boto3.client('rekognition')

def lambda_handler(event, context):
    # Get the object from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    
    try:
        # Only process image files
        if not key.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            print(f"Skipping non-image file: {key}")
            return {
                'statusCode': 200,
                'body': json.dumps('Not an image file')
            }
            
        # Detect labels in the image
        response = rekognition.detect_labels(
            Image={
                'S3Object': {
                    'Bucket': bucket,
                    'Name': key
                }
            },
            MaxLabels=10
        )
        
        # Extract labels
        labels = [label['Name'] for label in response['Labels']]
        
        # Add labels as metadata to the S3 object
        s3.put_object_tagging(
            Bucket=bucket,
            Key=key,
            Tagging={
                'TagSet': [
                    {
                        'Key': 'Labels',
                        'Value': ','.join(labels)
                    }
                ]
            }
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps(f'Successfully processed {key} and found labels: {labels}')
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error processing {key}: {str(e)}')
        }
