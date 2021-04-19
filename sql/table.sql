CREATE TABLE IF NOT EXISTS fruit(
    name VARCHAR PRIMARY KEY,
    count INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS public.user(
    id SERIAL PRIMARY KEY,
    account CHAR(50) UNIQUE,
    hashed_password CHAR(60),
    money INTEGER,
    is_platform boolean DEFAULT false
);

CREATE TABLE IF NOT EXISTS item(
    id SERIAL PRIMARY KEY,
    owner_id INTEGER NOT null,
    target_price INTEGER NOT null,
    project_content CHAR(1000),
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    project_name CHAR(100),
    representative CHAR(20),
    email CHAR(50),
    phone CHAR(20),
    FOREIGN KEY(owner_id) REFERENCES public.user(id)
);

CREATE TABLE IF NOT EXISTS donate_record(
    id SERIAL PRIMARY KEY,
    project_id INTEGER NOT null,
    donor_id INTEGER NOT null,
    money INTEGER,
    FOREIGN KEY(project_id) REFERENCES item(id),
    FOREIGN KEY(donor_id) REFERENCES public.user(id)
);

CREATE TABLE IF NOT EXISTS use_record(
    id SERIAL PRIMARY KEY,
    project_id INTEGER NOT null,
    money INTEGER,
    purpose CHAR(100),
    FOREIGN KEY(project_id) REFERENCES item(id)
);