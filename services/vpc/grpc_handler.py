from concurrent import futures
from typing import List

import grpc

from services.vpc import vpc_pb2_grpc, vpc_pb2
from services.vpc.models import SubnetModel, VpcModel, CreateSubnetRequest
from services.vpc.vpc import get_subnets_in_a_vpc, get_all_vpcs_based_on_region, create_vpc_with_subnets, create_subnet


class VpcService(vpc_pb2_grpc.VpcServiceServicer):
    def GetSubnetsInVpc(self, request, context):
        subnets_list: List[SubnetModel] = get_subnets_in_a_vpc(request.region, request.vpc_id)
        subnet_list_obj = []
        if subnets_list:
            for _subnet in subnets_list:
                subnet_list_obj.append(vpc_pb2.Subnet(
                    id=_subnet.Id,
                    name=_subnet.Name,
                    availability_zone=_subnet.AvailabilityZone,
                    cidr_block=_subnet.CidrBlock,
                    vpc_id=_subnet.VpcId,
                    route_table_id=_subnet.RouteTableId)
                )
            return subnet_list_obj
        else:
            return None

    def GetVpcBasedOnRegion(self, request, context):
        vpc_list: List[VpcModel] = get_all_vpcs_based_on_region(request.region, request.vpc_id)
        if vpc_list:
            for _vpc in vpc_list:
                vpc_obj = vpc_pb2.Vpc(
                    id=_vpc.Id,
                    name=_vpc.Name,
                    cidr_block=_vpc.CidrBlock,
                    region=_vpc.Region,
                )
                subnet_list_obj = []
                for _subnet in _vpc.Subnets:
                    subnet_list_obj.append(vpc_pb2.Subnet(
                        id=_subnet.Id,
                        name=_subnet.Name,
                        availability_zone=_subnet.AvailabilityZone,
                        cidr_block=_subnet.CidrBlock,
                        vpc_id=_subnet.VpcId,
                        route_table_id=_subnet.RouteTableId)
                    )
                vpc_obj.subnets = subnet_list_obj
            return vpc_list
        else:
            return None

    def CreateVpcWithSubnets(self, request, context):
        list_of_subnets = []
        for subnet in request.subnets:
            list_of_subnets.append(
                CreateSubnetRequest(
                    Region=subnet.region,
                    Name=subnet.name,
                    AvailabilityZone=subnet.availability_zone,
                    CidrBlock=subnet.cidr_block,
                    Access=subnet.access
                )
            )
        vpc: VpcModel = create_vpc_with_subnets(request.region, request.name, request.ip_cidr, list_of_subnets)
        print(vpc)
        if vpc:
            vpc_obj = vpc_pb2.Vpc(
                id=vpc.Id,
                name=vpc.Name,
                cidr_block=vpc.CidrBlock,
                region=vpc.Region
            )
            subnet_list_obj = []
            for _subnet in vpc.Subnets:
                subnet_list_obj.append(vpc_pb2.Subnet(
                    id=_subnet.Id,
                    name=_subnet.Name,
                    availability_zone=_subnet.AvailabilityZone,
                    cidr_block=_subnet.CidrBlock,
                    vpc_id=_subnet.VpcId,
                    route_table_id=_subnet.RouteTableId)
                )
            vpc_obj.subnets.extend(subnet_list_obj)
            return vpc_obj
        else:
            return None

    def CreateSubnet(self, request, context):
        subnet = create_subnet(request.region, request.name, request.az, request.cidr_block, request.vpc_id,
                               request.access)
        if subnet:
            return vpc_pb2.Subnet(
                id=subnet.Id,
                name=subnet.Name,
                availability_zone=subnet.AvailabilityZone,
                cidr_block=subnet.CidrBlock,
                vpc_id=subnet.VpcId,
                route_table_id=subnet.RouteTableId)
        else:
            return None


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    vpc_pb2_grpc.add_VpcServiceServicer_to_server(
        VpcService(), server)
    server.add_insecure_port('[::]:50052')
    print("Server started at port 50052")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
