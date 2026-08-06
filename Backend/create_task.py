import json
import uuid
import boto3
from datetime import datetime, timezone

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tasks')  # replace with your table name

CORS_HEADERS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Allow-Methods": "OPTIONS,POST"
}

def lambda_handler(event, context):
    try:
        body = json.loads(event.get('body') or '{}')
        title = body.get('title')
        description = body.get('description', '')

        if not title:
            return {
                'statusCode': 400,
                'headers': CORS_HEADERS,
                'body': json.dumps({'error': 'title is required'})
            }

        task_id = str(uuid.uuid4())
        created_at = datetime.now(timezone.utc).isoformat()

        item = {
            'taskId': task_id,
            'title': title,
            'description': description,
            'status': 'pending',
            'createdAt': created_at
        }

        table.put_item(Item=item)

        return {
            'statusCode': 201,
            'headers': CORS_HEADERS,
            'body': json.dumps({'task': item})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': CORS_HEADERS,
            'body': json.dumps({'error': str(e)})
        }