CREATE TABLE users (
    user_id VARCHAR(20),
    signup_date DATE,
    user_segment VARCHAR(50),
    city VARCHAR(50)
);

CREATE TABLE accounts (
    account_id VARCHAR(20),
    user_id VARCHAR(20),
    account_status VARCHAR(20),
    activation_date DATE
);

CREATE TABLE events (
    event_id VARCHAR(20),
    user_id VARCHAR(20),
    event_date DATE,
    event_name VARCHAR(50),
    feature_name VARCHAR(50),
    transaction_flag INTEGER
);
