import json

def lambda_handler(event, context):
    print("✅ Lambda triggered!")
    print(json.dumps(event, indent=2))
    return {
        'statusCode': 200,
        'body': json.dumps('Event received')
    }
import json

def lambda_handler(event, context):
    print("✅ Lambda triggered!")
    print(json.dumps(event, indent=2))
    return {
        'statusCode': 200,
        'body': json.dumps('Event received')
    }

