import json
import urllib3

http = urllib3.PoolManager()

def handler(event, context):
    print("Rekognition trigger received event:")
    print(json.dumps(event))

    response_url = event['ResponseURL']

    response_body = {
        'Status': 'SUCCESS',
        'Reason': 'See the logs in CloudWatch Log Stream: ' + context.log_stream_name,
        'PhysicalResourceId': context.log_stream_name,
        'StackId': event['StackId'],
        'RequestId': event['RequestId'],
        'LogicalResourceId': event['LogicalResourceId'],
        'Data': {}
    }

    json_response_body = json.dumps(response_body)

    headers = {
        'content-type': '',
        'content-length': str(len(json_response_body))
    }

    try:
        http.request('PUT', response_url, body=json_response_body, headers=headers)
        print("CloudFormation response sent.")
    except Exception as e:
        print("Failed to send response: ", str(e))

    return {
        'statusCode': 200,
        'body': json.dumps('Processed')
    }

