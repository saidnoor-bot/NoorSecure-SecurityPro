import json
import os
import urllib.request

def lambda_handler(event, context):
    symbol = event['queryStringParameters'].get('symbol', 'AAPL')
    api_key = os.environ['API_KEY']

    url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={api_key}"

    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())
            return {
                'statusCode': 200,
                'headers': {'Content-Type': 'application/json'},
                'body': json.dumps(data)
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

