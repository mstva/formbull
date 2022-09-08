#!/usr/bin/env python3

import aws_cdk as cdk

from crewtech_api.crewtech_api_stack import CrewtechApiStack


app = cdk.App()
CrewtechApiStack(app, "crewtech-api")

app.synth()
