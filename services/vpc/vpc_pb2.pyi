from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateSubnetRequest(_message.Message):
    __slots__ = ["access", "availability_zone", "cidr_block", "name", "region", "vpc_id"]
    ACCESS_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_ZONE_FIELD_NUMBER: _ClassVar[int]
    CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    VPC_ID_FIELD_NUMBER: _ClassVar[int]
    access: str
    availability_zone: str
    cidr_block: str
    name: str
    region: str
    vpc_id: str
    def __init__(self, region: _Optional[str] = ..., name: _Optional[str] = ..., availability_zone: _Optional[str] = ..., cidr_block: _Optional[str] = ..., vpc_id: _Optional[str] = ..., access: _Optional[str] = ...) -> None: ...

class CreateVpcRequest(_message.Message):
    __slots__ = ["ip_cidr", "name", "region", "subnets"]
    IP_CIDR_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    SUBNETS_FIELD_NUMBER: _ClassVar[int]
    ip_cidr: str
    name: str
    region: str
    subnets: _containers.RepeatedCompositeFieldContainer[CreateSubnetRequest]
    def __init__(self, region: _Optional[str] = ..., name: _Optional[str] = ..., ip_cidr: _Optional[str] = ..., subnets: _Optional[_Iterable[_Union[CreateSubnetRequest, _Mapping]]] = ...) -> None: ...

class ListOfSubnets(_message.Message):
    __slots__ = ["subnets"]
    SUBNETS_FIELD_NUMBER: _ClassVar[int]
    subnets: _containers.RepeatedCompositeFieldContainer[Subnet]
    def __init__(self, subnets: _Optional[_Iterable[_Union[Subnet, _Mapping]]] = ...) -> None: ...

class ListOfVpcs(_message.Message):
    __slots__ = ["vpc"]
    VPC_FIELD_NUMBER: _ClassVar[int]
    vpc: _containers.RepeatedCompositeFieldContainer[Vpc]
    def __init__(self, vpc: _Optional[_Iterable[_Union[Vpc, _Mapping]]] = ...) -> None: ...

class RegionAndVpcRequest(_message.Message):
    __slots__ = ["region", "vpc_id"]
    REGION_FIELD_NUMBER: _ClassVar[int]
    VPC_ID_FIELD_NUMBER: _ClassVar[int]
    region: str
    vpc_id: str
    def __init__(self, region: _Optional[str] = ..., vpc_id: _Optional[str] = ...) -> None: ...

class Subnet(_message.Message):
    __slots__ = ["availability_zone", "cidr_block", "id", "name", "route_table_id", "vpc_id"]
    AVAILABILITY_ZONE_FIELD_NUMBER: _ClassVar[int]
    CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ROUTE_TABLE_ID_FIELD_NUMBER: _ClassVar[int]
    VPC_ID_FIELD_NUMBER: _ClassVar[int]
    availability_zone: str
    cidr_block: str
    id: str
    name: str
    route_table_id: str
    vpc_id: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., availability_zone: _Optional[str] = ..., cidr_block: _Optional[str] = ..., vpc_id: _Optional[str] = ..., route_table_id: _Optional[str] = ...) -> None: ...

class Vpc(_message.Message):
    __slots__ = ["cidr_block", "id", "name", "region", "subnets"]
    CIDR_BLOCK_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    REGION_FIELD_NUMBER: _ClassVar[int]
    SUBNETS_FIELD_NUMBER: _ClassVar[int]
    cidr_block: str
    id: str
    name: str
    region: str
    subnets: _containers.RepeatedCompositeFieldContainer[Subnet]
    def __init__(self, id: _Optional[str] = ..., cidr_block: _Optional[str] = ..., name: _Optional[str] = ..., region: _Optional[str] = ..., subnets: _Optional[_Iterable[_Union[Subnet, _Mapping]]] = ...) -> None: ...
