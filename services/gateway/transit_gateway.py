import logging
from python_terraform import *
from botocore.exceptions import ClientError

from services.gateway.models import TransitGatewayModel
from services.vpc.utils import get_boto3_client

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

service = 'ec2'


def check_if_tgw_exists(region: str):
    client = get_boto3_client(service, region)

    try:
        response = client.describe_transit_gateways(Filters=[
            {
                'Name': 'state',
                'Values': ['available']
            }
        ])
        print(response)
        if response['TransitGateways']:
            tgw = response['TransitGateways'][0]   # just take the first one for now
            return TransitGatewayModel(Id=tgw['TransitGatewayId'],
                                       Arn=tgw['TransitGatewayArn'],
                                       OwnerId=tgw['OwnerId'],
                                       CreationTime=tgw['CreationTime'],
                                       Description=tgw['Description'],
                                       State=tgw['State'])
        else:
            return None
    except ClientError as e:
        logger.exception(e)


if __name__ == '__main__':
    check_if_tgw_exists(region='us-east-1')
