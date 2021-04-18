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
)