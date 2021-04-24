CREATE TABLE IF NOT EXISTS proposal(
    proposal_addr CHAR(42) NOT NULL PRIMARY KEY,
    owner_addr CHAR(42) NOT NULL,
    target_price INTEGER NOT NULL,
    project_description CHAR(1000),
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP NOT NULL,
    project_name CHAR(100),
    representative CHAR(20),
    email CHAR(50),
    phone CHAR(20)
);

CREATE TABLE IF NOT EXISTS image_list(
    id SERIAL PRIMARY KEY,
    proposal_addr CHAR(42) NOT NULL,
    image_url CHAR(200),
    FOREIGN KEY(proposal_addr) REFERENCES proposal(proposal_addr)
);

CREATE TABLE IF NOT EXISTS money_list(
    id SERIAL PRIMARY KEY,
    proposal_addr CHAR(42) NOT NULL,
    money INTEGER NOT NULL,
    FOREIGN KEY(proposal_addr) REFERENCES proposal(proposal_addr)
);
