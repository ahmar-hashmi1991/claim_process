from fastapi import APIRouter, HTTPException, Depends, Request
from sqlalchemy import func, select
from ...schemas import ClaimCreate, ProviderNetFee
from ...crud import create_claim
from sqlmodel import Session, select
from typing import List
from ...models import Claim
from ...dependencies import get_session
from datetime import datetime, timedelta

router = APIRouter()

@router.post("/", response_model=Claim)
def create_claim_endpoint(claim: ClaimCreate):
    try:
        result = create_claim(claim)
        return {"id": result.id, "net_fee": result.net_fee}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
# Define rate limit settings
RATE_LIMIT = 10  # 10 requests per minute

requests = []

# Define rate limiting dependency
async def rate_limiter(request: Request):
    now = datetime.now()
    minute_ago = now - timedelta(minutes=1)

    # Count requests within the last minute
    requests_in_last_minute = sum(
        1 for request_time in requests if request_time > minute_ago
    )

    if requests_in_last_minute >= RATE_LIMIT:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")

    # Add current request time to the list
    requests.append(now)

    # Return the request object
    return request

# Apply rate limiting dependency to the route
@router.get("/top-providers/", response_model=List[ProviderNetFee], dependencies=[Depends(rate_limiter)])
async def get_top_providers_with_rate_limit(session: Session = Depends(get_session)):
    try:
        statement = select(Claim.provider_npi,
                            func.sum(Claim.net_fee).label('total_net_fee')) \
            .group_by(Claim.provider_npi) \
            .order_by(func.sum(Claim.net_fee).desc()) \
            .limit(10)
        results = session.exec(statement).all()
        if not results:
            raise HTTPException(status_code=404, detail="No top providers found")
        return results
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
