import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tasks')  # replace with your table name

CORS_HEADERS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Allow-Methods": "OPTIONS,PUT"
}

def lambda_handler(event, context):
    try:
        task_id = event['pathParameters']['id']
        body = json.loads(event.get('body') or '{}')

        update_expr_parts = []
        expr_attr_values = {}
        expr_attr_names = {}

        # Allow updating title, description, and/or status
        for field in ['title', 'description', 'status']:
            if field in body:
                placeholder = f":{field}"
                name_placeholder = f"#{field}"
                update_expr_parts.append(f"{name_placeholder} = {placeholder}")
                expr_attr_values[placeholder] = body[field]
                expr_attr_names[name_placeholder] = field

        if not update_expr_parts:
            return {
                'statusCode': 400,
                'headers': CORS_HEADERS,
                'body': json.dumps({'error': 'No valid fields to update'})
            }

        update_expression = "SET " + ", ".join(update_expr_parts)

        response = table.update_item(
            Key={'taskId': task_id},
            UpdateExpression=update_expression,
            ExpressionAttributeValues=expr_attr_values,
            ExpressionAttributeNames=expr_attr_names,
            ReturnValues="ALL_NEW"
        )

        return {
            'statusCode': 200,
            'headers': CORS_HEADERS,
            'body': json.dumps({'task': response.get('Attributes')})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': CORS_HEADERS,
            'body': json.dumps({'error': str(e)})
        }
