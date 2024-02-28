# create lambda function and trigger event

import os
import boto3
import json
import datetime

event_client = boto3.client('events')

def handler(event, context):

    response = event_client.put_events(
        Entries=[
            {
                'Time': datetime.datetime.now(),
                'Source': 'Lambda Publish',
                'Resources': [
                ],
                'DetailType': 'Custom Event demo',
                # 'Detail': json.dumps(event),
                'Detail': '{ "name": "crazyfreaktwo", "salary": "101", "married": "true"}',
                # 'EventBusName': event_client.describe_rule(Name='custom-rule-demo')['Arn'],
                'EventBusName': 'custom-rule-demo', # manually set the event bus name,
                'TraceHeader': 'testdemo'
            }
        ]
    )

    print(response)

    return {
        'statusCode': 200,
        'body': json.dumps('EventBridge rule created successfully!')
    }