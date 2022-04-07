import aws_cdk as cdk
from constructs import Construct
from aws_cdk import (aws_apigateway as apigateway,
                     aws_lambda as lambda_,
                     aws_dynamodb)

class TasksService(Construct):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        task_table = aws_dynamodb.Table(
            self,
            "task_table",
            partition_key=aws_dynamodb.Attribute(
                name="id",
                type=aws_dynamodb.AttributeType.STRING
            )
        )

        task_lambda = lambda_.Function(
            self,
            "TaskLambda",
            runtime=lambda_.Runtime.PYTHON_3_9,
            code=lambda_.Code.from_asset("resources"),
            handler="tasks.main"
        )


        task_lambda.add_environment("TABLE_NAME", task_table.table_name)

        task_table.grant_read_write_data(task_lambda)

        taks_integration = apigateway.LambdaIntegration(task_lambda)

        api = apigateway.RestApi(
            self, "widgets-api",
            rest_api_name="Widget Service",
            description="This service serves widgets."
        )

        api.root.add_method("ANY", taks_integration)
