import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tasks')  # replace with your table name

CORS_HEADERS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Allow-Methods": "OPTIONS,DELETE"
}

def lambda_handler(event, context):
    try:
        task_id = event['pathParameters']['id']

        table.delete_item(Key={'taskId': task_id})

        return {
            'statusCode': 200,
            'headers': CORS_HEADERS,
            'body': json.dumps({'message': 'Task deleted', 'taskId': task_id})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': CORS_HEADERS,
            'body': json.dumps({'error': str(e)})
        }