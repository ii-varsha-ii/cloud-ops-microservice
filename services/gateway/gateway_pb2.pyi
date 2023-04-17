from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RegionRequest(_message.Message):
    __slots__ = ["region"]
    REGION_FIELD_NUMBER: _ClassVar[int]
    region: str
    def __init__(self, region: _Optional[str] = ...) -> None: ...

class TransitGateway(_message.Message):
    __slots__ = ["arn", "creation_time", "description", "id", "owner_id", "state"]
    ARN_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    OWNER_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    arn: str
    creation_time: str
    description: str
    id: str
    owner_id: str
    state: str
    def __init__(self, id: _Optional[str] = ..., arn: _Optional[str] = ..., state: _Optional[str] = ..., description: _Optional[str] = ..., owner_id: _Optional[str] = ..., creation_time: _Optional[str] = ...) -> None: ...
