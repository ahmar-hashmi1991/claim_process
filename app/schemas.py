from pydantic import BaseModel, Field
from typing import Optional

class ClaimCreate(BaseModel):
    service_date: str
    submitted_procedure: str = Field(..., pattern=r'^D.*')
    quadrant: Optional[str] = None
    plan_group_number: str
    subscriber_number: str
    provider_npi: str = Field(..., pattern=r'^\d{10}$')
    provider_fees: float
    allowed_fees: float
    member_coinsurance: float
    member_copay: float
    net_fee: Optional[float] = None

class ProviderNetFee(BaseModel):
    provider_npi: str = Field(..., pattern=r'^\d{10}$')
    total_net_fee: float

# This model assumes that your database query is returning a list of results
# with each item having 'provider_npi' and 'total_net_fee' fields.
