import json
import boto3

rekognition = boto3.client('rekognition')
sns = boto3.client('sns')

def lambda_handler(event, context):
    print("✅ Lambda triggered!")
    print(json.dumps(event))

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Call Rekognition to detect labels in the image
    response = rekognition.detect_labels(
        Image={'S3Object': {'Bucket': bucket, 'Name': key}},
        MaxLabels=5
    )

    labels = [label['Name'] for label in response['Labels']]
    print("🧠 Labels detected:", labels)

    # Compose SNS message
    message = f"📦 Image uploaded: {key}\n Bucket: {bucket}\n🔖 Labels: {', '.join(labels)}"

    # Publish message to SNS topic
    sns.publish(
        TopicArn='arn:aws:sns:us-east-1:429128462098:S3UploadAlerts',
        Subject='🚨 New S3 Upload with Labels',
        Message=message
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Success! Labels detected and SNS sent.')
    }

