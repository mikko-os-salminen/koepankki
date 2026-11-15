CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

CREATE TABLE tests (
    id INTEGER PRIMARY KEY,
    aine TEXT,
    aihe TEXT,
    vuosi INTEGER,
    koe TEXT,
    user_id INTEGER REFERENCES users
);