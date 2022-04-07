import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
TABLE_NAME = os.environ['TABLE_NAME']


def main(event, context):
    method = event['httpMethod']

    tasks_table = dynamodb.Table(TABLE_NAME)
    if method == 'GET':
        tasks = tasks_table.scan()['Items']
        return response(tasks)

    if method == 'POST':
        body = json.loads(event['body'])

        tasks_table.put_item(
            Item={
                'id': body['task']
            }
        )
        return response({"message":"Task created"})

    return response({"message":"Not found"})

def response(body, status_code = 200, headers = {}):
    return {
        "statusCode": status_code,
        "headers": headers,
        "body": json.dumps(body)
    }
