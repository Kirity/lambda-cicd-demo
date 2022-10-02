import json
import boto3

s3 = boto3.resource('s3')

def lambda_handler(event, context):
    print("version v3")
    print("S3 Buckets")
    print("-----------")
    for bucket in s3.buckets.all():
        print(bucket.name)
    print("-----------")
    return {
        "statusCode": 200
    }
