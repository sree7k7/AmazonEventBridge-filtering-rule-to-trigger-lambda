import datetime

def handler(event, context):
    # Your code here
    print('Event: ', event)
    return {
        'statusCode': 200,
        'body': 'Hello from Lambda!',
        'event': event
    }