from aws_cdk import (
    # Duration,
    RemovalPolicy,
    Stack,
    CfnOutput
    # aws_sqs as sqs,
)
from constructs import Construct
import aws_cdk.aws_s3 as s3
from aws_cdk import aws_lambda as lambda_
import aws_cdk.aws_iam as iam
from aws_cdk import aws_events as events
from aws_cdk import aws_events_targets as targets

class AmazonEventBridgeFilteringRuleToTriggerLambdaStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # IAM role for lambda function
        role = iam.Role(self, "LambdaRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole"),
                iam.ManagedPolicy.from_aws_managed_policy_name("AmazonEventBridgeFullAccess"),
            ],
        )

        # Create a lambda function to trigger EventBridge rule
        lambdaFn = lambda_.Function(self, "LambdaFunctionPushEvent",
            function_name="LambdaFunctionPushEvent",
            runtime=lambda_.Runtime.PYTHON_3_12,
            role=role,
            handler="lambda_trigger_event.handler",
            code=lambda_.Code.from_asset("lambda"), 
        )

        # # create a custom event bus
        event_bus = events.EventBus(self, "custom-rule-demo",
            event_bus_name="custom-rule-demo"
        )

        # # create the lambda funtion to read the custom event bus rule

        lambda_read_fn = lambda_.Function(self, "LambdaFunctionReadEvent",
            function_name="LambdaFunctionReadEvent",
            runtime=lambda_.Runtime.PYTHON_3_12,
            role=role,
            handler="lambda_read_event.handler",
            code=lambda_.Code.from_asset("lambda_read_event"), 
        )

        # # create a rule to filter events
        rule = events.Rule(self, "Rule",
            event_bus=event_bus,
            targets=[targets.LambdaFunction(lambda_read_fn)],
            rule_name="filtering-rule",
            description="Rule to filter events",
            event_pattern={
                "detail": {
                    "married": ["true"]
                }
            },
        )

        # # output the custom event bus name and role arn
        event_bus_name = CfnOutput(self, "EventBusName",
            value=event_bus.event_bus_name,
            description="Event Bus Name"
        )   

        event_bus_arn = CfnOutput(self, "EventBusArn",
            value=event_bus.event_bus_arn,
            description="Event Bus ARN"
        )





                                    
