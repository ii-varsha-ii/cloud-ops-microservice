import boto3


def get_boto3_resource(service: str, region: str):
    return boto3.resource(service, region_name=region)


def get_boto3_client(service: str, region: str):
    return boto3.client(service, region_name=region)
