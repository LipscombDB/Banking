
CREATE DATABASE IF NOT EXISTS BANK;

USE BANK;

DROP TABLE IF EXISTS Loan;
DROP TABLE IF EXISTS Transaction;
DROP TABLE IF EXISTS Account;
DROP TABLE IF EXISTS Customer;

CREATE TABLE Account(
    accountID INT NOT NULL AUTO_INCREMENT,
    Balances DECIMAL(32, 2),
    AccTypes VARCHAR(10),
    AccStatus VARCHAR(3),
    CustomerID INT,
    PRIMARY KEY (accountID),
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID) ON UPDATE CASCADE ON DELETE SET NULL
);

CREATE TABLE Customer(
    CustomerID INT NOT NULL AUTO_INCREMENT,
    FName varchar(50),
    LName varchar(50),
    email varchar(50),
    AccountID INT,
    PRIMARY KEY (CustomerID),
    FOREIGN KEY (AccountID) REFERENCES Account(accountID) ON UPDATE CASCADE ON DELETE SET NULL
);

CREATE TABLE Transaction(
    TransactionID INT NOT NULL AUTO_INCREMENT,
    TransAmount DECIMAL(32,2),
    TransType VARCHAR(15),
    TransDate TIMESTAMP,
    AccID INT,
    CustomerID INT,
    PRIMARY KEY (TransactionID),
    FOREIGN KEY (AccID) REFERENCES Account(accountID) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID) ON UPDATE CASCADE ON DELETE SET NULL
);

CREATE TABLE Loan(
    LoanID INT NOT NULL AUTO_INCREMENT,
    LoanAmm DECIMAL(32,2),
    InterestRate DOUBLE(3,2),
    LoanStatus VARCHAR(3),
    customerID INT,
    PRIMARY KEY (LoanID),
    FOREIGN KEY (customerID) REFERENCES Customer(CustomerID) ON UPDATE CASCADE ON DELETE SET NULL
);

