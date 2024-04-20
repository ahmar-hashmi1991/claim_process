from sqlmodel import Session, SQLModel
from .models import Claim
from . import engine

def create_claim(claim_data):
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        claim = Claim(**claim_data.dict())
        claim.net_fee = claim.compute_net_fee()
        session.add(claim)
        session.commit()
        session.refresh(claim)
        return claim