from sqlmodel import SQLModel, Field
import uuid
from typing import Optional

class Claim(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    service_date: str
    submitted_procedure: str
    quadrant: Optional[str] = None  # Now an optional field
    plan_group_number: str = Field(alias="Plan/Group #")
    subscriber_number: str = Field(alias="Subscriber#")
    provider_npi: str = Field(alias="Provider NPI")
    provider_fees: float
    allowed_fees: float
    member_coinsurance: float
    member_copay: float
    net_fee: float = Field(default=None)

    def compute_net_fee(self):
        return self.provider_fees + self.member_coinsurance + self.member_copay - self.allowed_fees