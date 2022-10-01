# Introduction

This project is a sample AWS Lambda function to print the S3 buckets in the account.

# Project files and structure

`src/lambda_function.py` : this file contains the business logic.

`buildspec.yaml`: this file contains the build instrcutions during the build phase of this project.

`cfn.yaml`: this is the CloudFormation template file to create the resources needed to provision the Lambda infrastructure.

`config.json`: this file will have the variable values provied to `cfn.yaml` file

`requirements.txt`: contains the list of dependencies needed for the Lambda function.


# What is happening in build file?




