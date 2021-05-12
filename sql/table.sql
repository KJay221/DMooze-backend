CREATE TABLE IF NOT EXISTS proposal(
    proposal_id INTEGER PRIMARY KEY,
    owner_addr CHAR(42) NOT NULL,
    target_price INTEGER NOT NULL,
    project_description CHAR(1000),
    start_time TIMESTAMP NOT NULL,
    project_name CHAR(100),
    representative CHAR(20),
    email CHAR(50),
    phone CHAR(20)
);

CREATE TABLE IF NOT EXISTS image_list(
    id SERIAL PRIMARY KEY,
    proposal_id INTEGER NOT NULL,
    image_url CHAR(400),
    FOREIGN KEY(proposal_id) REFERENCES proposal(proposal_id)
);

CREATE TABLE IF NOT EXISTS money_list(
    id SERIAL PRIMARY KEY,
    proposal_id INTEGER NOT NULL,
    money INTEGER NOT NULL,
    FOREIGN KEY(proposal_id) REFERENCES proposal(proposal_id)
);
