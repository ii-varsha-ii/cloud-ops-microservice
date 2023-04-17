from typing import List, Optional

from pydantic import BaseModel


class SubnetModel(BaseModel):
    Id: str
    Name: Optional[str]
    AvailabilityZone: str
    CidrBlock: str
    VpcId: Optional[str]
    RouteTableId: Optional[str]


class VpcModel(BaseModel):
    Id: str
    CidrBlock: str
    Name: Optional[str]
    Region: str
    Subnets: List[SubnetModel] = []


class InternetGatewayModel(BaseModel):
    Id: str
    Attachments: List


class CreateSubnetRequest(BaseModel):
    Region: str
    Name: str
    AvailabilityZone: str
    CidrBlock: str
    VpcId: Optional[str]
    Access: str
