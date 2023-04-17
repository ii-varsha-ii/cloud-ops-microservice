from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TransitGatewayModel(BaseModel):
    Id: Optional[str]
    Arn: Optional[str]
    State: Optional[str]
    OwnerId: Optional[str]
    Description: Optional[str]
    CreationTime: Optional[datetime]
