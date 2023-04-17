from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel


class OrganizationModel(BaseModel):
    Id: str
    Arn: str
    MasterAccountArn: str
    MasterAccountId: str
    MasterAccountEmail: str


class AccountModel(BaseModel):
    Id: str
    Arn: str
    Email: str
    Name: str
    Status: str
    JoinedMethod: str
    JoinedTimestamp: datetime


class InviteAccountResponseModel(BaseModel):
    Id: str
    Arn: str
    Parties: List
    State: str
    RequestedTimestamp: datetime
    ExpirationTimestamp: datetime
    Action: str
