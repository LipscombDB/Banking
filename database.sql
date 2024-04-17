-- Drop the existing tables if they exist
DROP TABLE IF EXISTS Transaction;
DROP TABLE IF EXISTS Loan;
DROP TABLE IF EXISTS Customer;
DROP TABLE IF EXISTS Account;

-- Create the Account table
CREATE TABLE Account (
    accountID INT NOT NULL AUTO_INCREMENT,
    Balances DECIMAL(32, 2),
    AccType VARCHAR(10),
    AccStatus VARCHAR(10),
    PRIMARY KEY (accountID)
);

-- Create the Customer table
CREATE TABLE Customer (
    CustomerID INT NOT NULL AUTO_INCREMENT,
    FName VARCHAR(50),
    LName VARCHAR(50),
    email VARCHAR(50),
    PRIMARY KEY (CustomerID)
);

-- Create the Transaction table
CREATE TABLE Transaction (
    TransactionID INT NOT NULL AUTO_INCREMENT,
    TransAmount DECIMAL(32, 2),
    TransType VARCHAR(15),
    TransDate TIMESTAMP,
    AccID INT,
    CustomerID INT,
    PRIMARY KEY (TransactionID),
    FOREIGN KEY (AccID) REFERENCES Account(accountID) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID) ON UPDATE CASCADE ON DELETE SET NULL
);

-- Create the Loan table
CREATE TABLE Loan (
    LoanID INT NOT NULL AUTO_INCREMENT,
    LoanAmount DECIMAL(32, 2),
    InterestRate DOUBLE,
    LoanStatus VARCHAR(10),
    CustomerID INT,
    PRIMARY KEY (LoanID),
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID) ON UPDATE CASCADE ON DELETE SET NULL
);
