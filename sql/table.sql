CREATE TABLE IF NOT EXISTS proposal(
    proposal_id CHAR(36) PRIMARY KEY,
    owner_addr CHAR(42) NOT NULL,
    target_price DOUBLE PRECISION NOT NULL,
    project_description CHAR(1000) NOT NULL,
    start_time TIMESTAMP NOT NULL,
    project_name CHAR(100) NOT NULL,
    representative CHAR(20) NOT NULL,
    email CHAR(50) NOT NULL,
    phone CHAR(20) NOT NULL,
    create_hash CHAR(66) NOT NULL
);

CREATE TABLE IF NOT EXISTS image_list(
    id CHAR(36) PRIMARY KEY,
    proposal_id CHAR(36) NOT NULL,
    image_url CHAR(400) NOT NULL,
    FOREIGN KEY(proposal_id) REFERENCES proposal(proposal_id)
);

CREATE TABLE IF NOT EXISTS money_list(
    id CHAR(36) PRIMARY KEY,
    proposal_id CHAR(36) NOT NULL,
    money DOUBLE PRECISION NOT NULL,
    sponsor_addr CHAR(42) NOT NULL,
    transaction_hash CHAR(66) NOT NULL,
    input_time TIMESTAMP NOT NULL,
    FOREIGN KEY(proposal_id) REFERENCES proposal(proposal_id)
);

CREATE TABLE IF NOT EXISTS withdrawal_list(
    id CHAR(36) PRIMARY KEY,
    proposal_id CHAR(36) NOT NULL,
    money DOUBLE PRECISION NOT NULL,
    use_description CHAR(1000) NOT NULL,
    transaction_hash CHAR(66) NOT NULL,
    output_time TIMESTAMP NOT NULL,
    FOREIGN KEY(proposal_id) REFERENCES proposal(proposal_id)
);
