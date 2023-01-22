#!/usr/bin/env python3

import aws_cdk as cdk

from cdkcicd.cdkcicd_stack import CdkcicdStack


app = cdk.App()
CdkcicdStack(app, "cdkcicd")

app.synth()
