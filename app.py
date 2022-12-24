#!/usr/bin/env python3

from aws_cdk import App, Stack, aws_apigateway
from constructs import Construct

from routes.form_routes import form_routes
from stacks.form_stack import FormStack
from utils.constants import app_name


class FormbullStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        api_name = f"{app_name}_routes"
        api = aws_apigateway.RestApi(scope=self, id=api_name, rest_api_name=api_name,)

        form_stack = FormStack(scope=self)
        form_routes(api, form_stack)


app = App()
FormbullStack(
    scope=app,
    construct_id="FormbullStack",
    description="Formbull API Main Stack."
)
app.synth()
