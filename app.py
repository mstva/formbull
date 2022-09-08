#!/usr/bin/env python3

from aws_cdk import App, Stack
from constructs import Construct


class CrewtechApiStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


app = App()
CrewtechApiStack(
    scope=app,
    construct_id="CrewtechApiStack",
    description="CrewTech API Main Stack."
)
app.synth()
