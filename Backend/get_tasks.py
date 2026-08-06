import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tasks')  # replace with your table name

CORS_HEADERS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Allow-Methods": "OPTIONS,GET"
}

def lambda_handler(event, context):
    try:
        response = table.scan()
        tasks = response.get('Items', [])

        # Handle pagination if table grows beyond one page
        while 'LastEvaluatedKey' in response:
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            tasks.extend(response.get('Items', []))

        # Sort newest first
        tasks.sort(key=lambda t: t.get('createdAt', ''), reverse=True)

        return {
            'statusCode': 200,
            'headers': CORS_HEADERS,
            'body': json.dumps({'tasks': tasks})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': CORS_HEADERS,
            'body': json.dumps({'error': str(e)})
        }
