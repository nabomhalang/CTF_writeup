CREATE TABLE users (
    uid INTEGER PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    token TEXT NOT NULL UNIQUE
);

CREATE TABLE memo (
    idx INTEGER PRIMARY KEY,
    uid INTEGER NOT NULL,
    text TEXT NOT NULL
);