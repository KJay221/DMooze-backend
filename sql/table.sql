CREATE TABLE IF NOT EXISTS proposal(
    id SERIAL PRIMARY KEY,
    owner_addr CHAR(64) NOT null,
    target_price INTEGER NOT null,
    project_description CHAR(1000),
    start_time TIMESTAMPTZ NOT NULL,
    end_time TIMESTAMPTZ NOT NULL,
    project_name CHAR(100),
    representative CHAR(20),
    email CHAR(50),
    phone CHAR(20)
);

CREATE TABLE IF NOT EXISTS image_list(
    id SERIAL PRIMARY KEY,
    proposal_id INTEGER NOT null,
    image_url CHAR(200),
    FOREIGN KEY(proposal_id) REFERENCES proposal(id)
);

SET timezone = 'Asia/Taipei';