CREATE DATABASE atm_db;

USE atm_db;

CREATE TABLE accounts (
    account_no INT PRIMARY KEY,
    pin INT,
    balance FLOAT
);

INSERT INTO accounts (account_no, pin, balance) VALUES (1234, 1111, 1000);
INSERT INTO accounts (account_no, pin, balance) VALUES (12341, 1111, 25000);
INSERT INTO accounts (account_no, pin, balance) VALUES (12342, 2222, 10000);
INSERT INTO accounts (account_no, pin, balance) VALUES (12343, 3333, 9850);
INSERT INTO accounts (account_no, pin, balance) VALUES (12344, 4444, 2541);
INSERT INTO accounts (account_no, pin, balance) VALUES (12345, 5555, 37810);

SELECT * FROM accounts;