from app.models import Claim

def test_claim_model():
    claim_data = {
        "service_date": "2024-04-20",
        "submitted_procedure": "D0180",
        "quadrant": None,
        "plan_group_number": "GRP-1000",
        "subscriber_number": "3730189502",
        "provider_npi": "1497775530",
        "provider_fees": 100.00,
        "allowed_fees": 100.00,
        "member_coinsurance": 0.00,
        "member_copay": 0.00
    }
    claim = Claim(**claim_data)
    assert claim.service_date == "2024-04-20"
    assert claim.submitted_procedure == "D0180"
    assert claim.quadrant == None
    assert claim.plan_group_number == "GRP-1000"
    assert claim.subscriber_number == "3730189502"
    assert claim.provider_npi == "1497775530"
    assert claim.provider_fees == 100.00
    assert claim.allowed_fees == 100.00
    assert claim.member_coinsurance == 0.00
    assert claim.member_copay == 0.00