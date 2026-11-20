BEGIN;
DROP TABLE IF EXISTS appointments;
DROP TABLE IF EXISTS services;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    role TEXT NOT NULL DEFAULT 'client'
);

CREATE TABLE services (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL CHECK (length(trim(name)) > 0),
    category TEXT NOT NULL DEFAULT 'General',
    duration_minutes INTEGER NOT NULL CHECK (duration_minutes > 0),
    price_cents INTEGER NOT NULL CHECK (price_cents >= 0),
    active INTEGER NOT NULL DEFAULT 1 CHECK (active IN (0, 1))
);

CREATE TABLE appointments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    service_id INTEGER NOT NULL,
    client_name TEXT NOT NULL,
    date TEXT NOT NULL CHECK (date GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'),
    time TEXT NOT NULL,
    stylist TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'Pending',
    notes TEXT,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (service_id) REFERENCES services(id)
);

INSERT INTO services (name, category, duration_minutes, price_cents) VALUES
    ('Haircut', 'Cutting', 30, 3000),
    ('Hair Coloring', 'Color', 90, 8000),
    ('Hair Styling', 'Styling', 45, 4500),
    ('Blowout', 'Styling', 40, 4000),
    ('Deep Conditioning', 'Treatment', 30, 2500),
    ('Highlights', 'Color', 120, 9500);

INSERT INTO appointments (service_id, client_name, date, time, stylist, status) VALUES
    (2, 'Jordan Lee', '2026-12-15', '9:00 AM', 'Sophia', 'Confirmed'),
    (1, 'Jordan Lee', '2026-12-15', '10:30 AM', 'Alex', 'Confirmed');

INSERT INTO appointments (service_id, client_name, date, time, stylist) VALUES
    (3, 'Jordan Lee', '2026-12-20', '1:00 PM', 'Sophia');
COMMIT;
