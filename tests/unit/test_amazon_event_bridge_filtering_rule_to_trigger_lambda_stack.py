import aws_cdk as core
import aws_cdk.assertions as assertions

from amazon_event_bridge_filtering_rule_to_trigger_lambda.amazon_event_bridge_filtering_rule_to_trigger_lambda_stack import AmazonEventBridgeFilteringRuleToTriggerLambdaStack

# example tests. To run these tests, uncomment this file along with the example
# resource in amazon_event_bridge_filtering_rule_to_trigger_lambda/amazon_event_bridge_filtering_rule_to_trigger_lambda_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AmazonEventBridgeFilteringRuleToTriggerLambdaStack(app, "amazon-event-bridge-filtering-rule-to-trigger-lambda")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
