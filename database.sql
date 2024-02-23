CREATE TABLE Customer(
    CustomerID  INT NOT NULL AUTO_INCREMENT UNIQUE,
    FName varchar(50),
    LName varchar(50),
    email varchar(50),
    AccountID INT,
    PRIMARY KEY (CustomerID),
    FOREIGN KEY (AccountID) REFERENCES Account(accountID) ON UPDATE CASCADE ON DELETE SET NULL
    );
   
CREATE TABLE Account(
    accountID INT NOT NULL AUTO_INCREMENT UNIQUE,
    Balances DECIMAL( 32, 2) ,
    AccTypes VARCHAR(10),
    AccStatus VARCHAR(3),
    CustomerID   INT,
    PRIMARY KEY (accountID),
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID) ON UPDATE CASCADE ON DELETE SET NULL
);

CREATE TABLE Transaction(
    TransactionID   INT NOT NULL AUTO_INCREMENT UNIQUE,
    TransAmount     DECIMAL(32,2),
    TransType       VARCHAR(15),
    TransDate       TIMESTAMP,
    AccID           INT,
    CustomerID      INT,
    PRIMARY KEY (TransactionID),
    FOREIGN KEY (AccID) REFERENCES Account(accountID) ON UPDATE CASCADE ON DELETE SET NULL,
    FOREIGN KEY (customerID) REFERENCES Customer(CustomerID) ON UPDATE CASCADE ON DELETE SET NULL
);

CREATE TABLE Loan(
    LoanID INT NOT NULL AUTO_INCREMENT UNIQUE,
    LoanAmm DECIMAL(32,2),
    InterestRate DOUBLE(3,2),
    LoanStatus VARCHAR(3),
    customerID   INT,
    AccID INT,
PRIMARY KEY (LoanID),
FOREIGN KEY (customerID) REFERENCES Customer(CustomerID) ON UPDATE CASCADE ON DELETE SET NULL,
FOREIGN KEY (AccID) REFERENCES Account(accountID) ON UPDATE CASCADE ON DELETE SET NULL
);
