import unittest

import boto3

from services.vpc.models import VpcModel, SubnetModel, CreateSubnetRequest
from services.vpc.vpc import create_vpc_with_subnets, get_all_vpcs_based_on_region, get_subnets_in_a_vpc


class TestOrganization(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_create_vpc(self):
        subnets = [
            CreateSubnetRequest(
                Region='us-east-1',
                Name='pub_subnet',
                AvailabilityZone='us-east-1a',
                CidrBlock='172.32.128.0/25',
                Access='public'
            ),
            CreateSubnetRequest(
                Region='us-east-1',
                Name='pri_subnet',
                AvailabilityZone='us-east-1b',
                CidrBlock='172.32.128.128/25',
                Access='private'
            )
        ]
        res = create_vpc_with_subnets(region='us-east-1', name='second_vpc', ip_cidr='172.32.128.0/24', subnets=subnets)
        self.assertIsNotNone(res)

    def test_get_vpc_based_on_region(self):
        res = get_all_vpcs_based_on_region(region='us-east-1', vpc_id=None)
        self.assertIsNotNone(res)

        res = get_all_vpcs_based_on_region(region='us-east-1', vpc_id='vpc-0aaf26ceef1245acc')
        print(res)
        if res:
            self.assertIsInstance(res[0], VpcModel)

    def test_get_subnets_in_a_vpc(self):
        res = get_subnets_in_a_vpc(region='us-east-1', vpc_id='vpc-0a052116d0198856a')
        if res:
            self.assertIsInstance(res[0], SubnetModel)