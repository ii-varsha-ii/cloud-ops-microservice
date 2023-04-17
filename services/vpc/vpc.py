import logging
import time
from typing import List, Optional

from botocore.exceptions import ClientError

from services.vpc.models import VpcModel, SubnetModel, InternetGatewayModel, CreateSubnetRequest
from services.vpc.utils import get_boto3_client, get_boto3_resource

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

service = 'ec2'


def __get_internet_gateway(region: str):
    """
    Get Internet Gateway in a region.
    :param region:
    :return: internet_gateway_id else, None
    """
    client = get_boto3_client(service=service, region=region)
    try:
        list_of_igw = client.describe_internet_gateways()
        if len(list_of_igw['InternetGateways']) == 1:
            igw = list_of_igw['InternetGateways'][0]
            return InternetGatewayModel(
                Id=igw['InternetGatewayId'],
                Attachments=igw['Attachments']
            )
        elif len(list_of_igw['InternetGateways']) == 0:
            return None
        else:
            raise Exception(f'Multiple Internet Gateways in the same region: {region}')
    except ClientError as e:
        logger.exception('An exception was raised while getting internet gateway', e)


def __create_internet_gateway(region: str) -> InternetGatewayModel:
    """
    Create Internet Gateway in a region
    :param region
    :return:
    """
    client = get_boto3_resource(service=service, region=region)
    try:
        igw = client.create_internet_gateway()
        logger.info(f'Internet Gateway created: {igw}')
        return InternetGatewayModel(
            Id=igw.internet_gateway_id,
            Attachments=igw.attachments
        )
    except ClientError as e:
        logger.exception('An exception was raised while creating internet gateway', e)


def __create_routing_table_and_associate(vpc_client, subnet_id: str, name: str, access):
    try:
        route_table = vpc_client.create_route_table(TagSpecifications=[
            {
                'ResourceType': 'route-table',
                'Tags': [
                    {
                        'Key': "Name",
                        'Value': access + '_' + name
                    },
                ]
            },
        ])
        logger.info(f"Route table created: {route_table}")
        response = route_table.associate_with_subnet(SubnetId=subnet_id)
        logger.info(f"Route table {route_table} associated with {subnet_id}")
        return route_table
    except ClientError as e:
        logger.exception('Could not create a routing table', e)


def create_subnet(region: str, name: str, availability_zone: str, cidr_block: str, vpc_id: str, access: str):
    """
    Create a subnet in the given vpc in a region.
    Create a routing table for the subnet.
    If the subnet is a public subnet, create or get an internet gateway and
    attach it to the subnet by creating a route between the igw and subnet
    else return

    :param region:
    :param name:
    :param availability_zone:
    :param cidr_block:
    :param vpc_id:
    :param access:
    :return:
    """
    client = get_boto3_resource(service=service, region=region)
    try:
        subnet = client.create_subnet(CidrBlock=cidr_block,
                                      VpcId=vpc_id,
                                      AvailabilityZone=availability_zone,
                                      TagSpecifications=[{
                                          'ResourceType': 'subnet',
                                          'Tags': [{'Key': 'Name', 'Value': name + "_" + access}]}
                                      ])

        vpc_client = client.Vpc(vpc_id)
        # create a route table for the subnet
        route_table = __create_routing_table_and_associate(vpc_client=vpc_client,
                                                           subnet_id=subnet.id,
                                                           name=name,
                                                           access=access)
        logger.info(f'route table created and associated for subnet {subnet}')

        if access == 'public':
            igw: InternetGatewayModel = __create_internet_gateway(region)
            # attach the igw with the vpc
            attach_with_vpc = vpc_client.attach_internet_gateway(InternetGatewayId=igw.Id)

            # create a route in the subnet routing table to allow traffic from igw
            route = route_table.create_route(DestinationCidrBlock='0.0.0.0/0',
                                             GatewayId=igw.Id)
            logger.info(f'route created between subnet {subnet} and internet gateway {igw.Id}')

        return SubnetModel(Id=subnet.id,
                           Name=name,
                           AvailabilityZone=subnet.availability_zone,
                           CidrBlock=subnet.cidr_block,
                           VpcId=subnet.vpc_id,
                           RouteTableId=route_table.id)
    except ClientError as e:
        logger.exception("func create_subnet failed with error: ", e)


def create_vpc_with_subnets(region: str, name: str, ip_cidr: str, subnets: List[CreateSubnetRequest]) -> Optional[VpcModel]:
    client = get_boto3_resource(service=service, region=region)
    try:
        vpc = client.create_vpc(CidrBlock=ip_cidr,
                                InstanceTenancy='default',
                                TagSpecifications=[{
                                    'ResourceType': 'vpc',
                                    'Tags': [{'Key': 'Name', 'Value': name}]}])
        vpc.wait_until_available()
        time.sleep(10)
        if vpc:
            vpc_model = VpcModel(Id=vpc.id, Name=name, CidrBlock=vpc.cidr_block, Region=region)
            if subnets:
                list_of_subnets = []
                for _subnet in subnets:
                    subnet = create_subnet(region=region, name=_subnet.Name, availability_zone=_subnet.AvailabilityZone,
                                           cidr_block=_subnet.CidrBlock, vpc_id=vpc.id,
                                           access=_subnet.Access)
                    list_of_subnets.append(subnet)
                vpc_model.Subnets = list_of_subnets
            logging.info(f"Response: {vpc_model}")
            return vpc_model
        else:
            return None
    except ClientError as e:
        logger.exception("func create_vpc_with_subnets failed with error: ", e)


def get_all_vpcs_based_on_region(region: str, vpc_id: Optional[str]) -> List[VpcModel]:
    client = get_boto3_client(service=service, region=region)
    try:
        if vpc_id:
            vpc_response = client.describe_vpcs(VpcIds=[vpc_id])
        else:
            vpc_response = client.describe_vpcs()
        if vpc_response['Vpcs']:
            plain_vpc_list = vpc_response['Vpcs']
            vpc_list = []
            for _vpc in plain_vpc_list:
                vpc_obj = VpcModel(CidrBlock=_vpc['CidrBlock'], Id=_vpc['VpcId'], Region=region)
                if 'Tags' in _vpc:
                    vpc_obj.Name = _vpc['Tags'][0]['Value']
                subnet_response = client.describe_subnets(Filters=[
                    {
                        'Name': 'vpc-id',
                        'Values': [_vpc['VpcId']]
                    }
                ])
                subnets_list = []
                if subnet_response['Subnets']:
                    plain_subnets_list = subnet_response['Subnets']
                    for _subnet in plain_subnets_list:
                        subnet_obj = SubnetModel(CidrBlock=_subnet['CidrBlock'], Id=_subnet['SubnetId'],
                                                 VpcId=_subnet['VpcId'], AvailabilityZone=_subnet['AvailabilityZone'])
                        if 'Tags' in _subnet:
                            subnet_obj.Name = _subnet['Tags'][0]['Value']

                        route_table_response = client.describe_route_tables(
                            Filters=[{'Name': 'association.subnet-id',
                                      'Values': [_subnet['SubnetId']]}])
                        if route_table_response['RouteTables']:
                            plain_route_tables = route_table_response['RouteTables']
                            subnet_obj.RouteTableId = plain_route_tables[0]['RouteTableId']
                        subnets_list.append(subnet_obj)
                vpc_obj.Subnets = subnets_list
                vpc_list.append(vpc_obj)
            return vpc_list
        else:
            return []
    except ClientError as e:
        logger.exception("func get_vpc_based_on_region failed with error: ", e)


def get_subnets_in_a_vpc(region: str, vpc_id: str) -> List[SubnetModel]:
    client = get_boto3_client(service=service, region=region)
    try:
        response = client.describe_subnets(Filters=[
            {
                'Name': 'vpc-id',
                'Values': [vpc_id]
            }
        ])
        subnets_list: List[SubnetModel] = []
        if response:
            plain_subnets_list = response['Subnets']
            for _subnet in plain_subnets_list:
                subnet_obj = SubnetModel(CidrBlock=_subnet['CidrBlock'], Id=_subnet['SubnetId'], VpcId=_subnet['VpcId'],
                                         AvailabilityZone=_subnet['AvailabilityZone'])
                if 'Tags' in _subnet:
                    subnet_obj.Name = _subnet['Tags'][0]['Value']
                subnets_list.append(subnet_obj)
        return subnets_list
    except ClientError as e:
        logger.exception("func get_subnets_in_a_vpc failed with error: ", e)
