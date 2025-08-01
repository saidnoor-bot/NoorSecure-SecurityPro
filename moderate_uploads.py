import boto3
import json

rekognition = boto3.client('rekognition')
sns = boto3.client('sns')

SNS_TOPIC_ARN = "arn:aws:sns:us-east-1:429128462098:ImageAlertTopic"

def lambda_handler(event, context):
    print("Event:", json.dumps(event))
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    response = rekognition.detect_moderation_labels(
        Image={'S3Object': {'Bucket': bucket, 'Name': key}},
        MinConfidence=80
    )

    labels = response['ModerationLabels']
    if labels:
        message = f"⚠️ Image '{key}' in bucket '{bucket}' flagged with labels: {[label['Name'] for label in labels]}"
        sns.publish(TopicArn=SNS_TOPIC_ARN, Message=message)

    return {
        'statusCode': 200,
        'body': json.dumps('Moderation complete')
    }
