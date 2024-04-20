-- init.sql
CREATE TABLE IF NOT EXISTS claim (
    id UUID PRIMARY KEY,
    service_date DATE,
    submitted_procedure VARCHAR(100),
    quadrant VARCHAR(10),
    plan_group_number VARCHAR(100),
    subscriber_number VARCHAR(100),
    provider_npi VARCHAR(100),
    provider_fees DECIMAL,
    allowed_fees DECIMAL,
    member_coinsurance DECIMAL,
    member_copay DECIMAL,
    net_fee DECIMAL
);
