from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Account(_message.Message):
    __slots__ = ["arn", "email", "id", "joined_method", "joined_timestamp", "name", "status"]
    ARN_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    JOINED_METHOD_FIELD_NUMBER: _ClassVar[int]
    JOINED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    arn: str
    email: str
    id: str
    joined_method: str
    joined_timestamp: str
    name: str
    status: str
    def __init__(self, id: _Optional[str] = ..., arn: _Optional[str] = ..., email: _Optional[str] = ..., name: _Optional[str] = ..., status: _Optional[str] = ..., joined_method: _Optional[str] = ..., joined_timestamp: _Optional[str] = ...) -> None: ...

class AccountId(_message.Message):
    __slots__ = ["account_id"]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    def __init__(self, account_id: _Optional[str] = ...) -> None: ...

class InviteAccountRequest(_message.Message):
    __slots__ = ["account_id", "email_id"]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ID_FIELD_NUMBER: _ClassVar[int]
    account_id: str
    email_id: str
    def __init__(self, account_id: _Optional[str] = ..., email_id: _Optional[str] = ...) -> None: ...

class InviteAccountResponse(_message.Message):
    __slots__ = ["action", "arn", "expiration_timestamp", "id", "parties", "requested_timestamp", "state"]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    ARN_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    PARTIES_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    action: str
    arn: str
    expiration_timestamp: str
    id: str
    parties: _containers.RepeatedCompositeFieldContainer[Pair]
    requested_timestamp: str
    state: str
    def __init__(self, id: _Optional[str] = ..., arn: _Optional[str] = ..., parties: _Optional[_Iterable[_Union[Pair, _Mapping]]] = ..., state: _Optional[str] = ..., requested_timestamp: _Optional[str] = ..., expiration_timestamp: _Optional[str] = ..., action: _Optional[str] = ...) -> None: ...

class ListOfAccounts(_message.Message):
    __slots__ = ["accounts"]
    ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    accounts: _containers.RepeatedCompositeFieldContainer[Account]
    def __init__(self, accounts: _Optional[_Iterable[_Union[Account, _Mapping]]] = ...) -> None: ...

class Organization(_message.Message):
    __slots__ = ["arn", "id", "master_account_arn", "master_account_email", "master_account_id"]
    ARN_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MASTER_ACCOUNT_ARN_FIELD_NUMBER: _ClassVar[int]
    MASTER_ACCOUNT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    MASTER_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    arn: str
    id: str
    master_account_arn: str
    master_account_email: str
    master_account_id: str
    def __init__(self, id: _Optional[str] = ..., arn: _Optional[str] = ..., master_account_arn: _Optional[str] = ..., master_account_id: _Optional[str] = ..., master_account_email: _Optional[str] = ...) -> None: ...

class Pair(_message.Message):
    __slots__ = ["Id", "Type"]
    ID_FIELD_NUMBER: _ClassVar[int]
    Id: str
    TYPE_FIELD_NUMBER: _ClassVar[int]
    Type: str
    def __init__(self, Id: _Optional[str] = ..., Type: _Optional[str] = ...) -> None: ...
