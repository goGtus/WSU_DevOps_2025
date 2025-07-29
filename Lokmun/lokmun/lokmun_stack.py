'''from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct

class LokmunStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "LokmunQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )'''

from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_events as events,
    aws_events_targets as targets,
    Duration
)
from constructs import Construct

class LokmunStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Define the Lambda function
        canary_fn = _lambda.Function(
            self, "CanaryFunction",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="mylambda.lambda_handler",  # filename.function_name
            code=_lambda.Code.from_asset("lambda"),  # folder containing mylambda.py
            timeout=Duration.seconds(10)
        )

        # Schedule the function to run every 5 minutes
        schedule = events.Rule(
            self, "ScheduleRule",
            schedule=events.Schedule.rate(Duration.minutes(5))
        )

        schedule.add_target(targets.LambdaFunction(canary_fn))
