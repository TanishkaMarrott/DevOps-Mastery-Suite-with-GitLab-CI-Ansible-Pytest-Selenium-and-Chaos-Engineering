import json

def lambda_handler(event, context):
    message = 'Hello, {}!'.format(event['name'])
    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }
