from aws_cdk import aws_lambda, aws_apigateway
from constructs import Construct

from ..utils.constants import app_name


def create_lambda_function(scope: Construct, handler: str):
    functions_path = "functions"
    functions_name = app_name + "_" + handler.split(".")[1] + "_function"

    _function = aws_lambda.Function(
        scope=scope,
        id=functions_name,
        function_name=functions_name,
        runtime=aws_lambda.Runtime.PYTHON_3_9,
        code=aws_lambda.Code.from_asset(functions_path),
        handler=handler,
    )

    return aws_apigateway.LambdaIntegration(_function)
