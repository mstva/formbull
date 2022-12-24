#!/usr/bin/env python3

from aws_cdk import App, Stack, aws_apigateway
from constructs import Construct


class FormbullStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


app = App()
FormbullStack(
    scope=app,
    construct_id="FormbullStack",
    description="Formbull API Main Stack."
)
app.synth()
