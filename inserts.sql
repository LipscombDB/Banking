-- Insert statements for the Customer table
INSERT INTO Customer(FName, LName, email, AccountID)
VALUES
    ('Spongebob', 'Squarepants', 'spsqaurepants@bikinibottom.com', 1234),
    ('Patrick', 'Star', 'patstar@bikinibottom.com', 4321),
    ('Lewis', 'Hamilton', 'benzbetter@mercedes.com', 6222),
    ('Max', 'Verstappen', 'maxverstappen@redbull.com', 3351);

-- Insert statements for the Account table
INSERT INTO Account(accountID, Balances, AccTypes, AccStatus, CustomerID)
VALUES 
    (1234, 0, 'Checking', 'Frozen', 1111),
    (4321, 100000000, 'Savings', 'Good', 1112),
    (6222, 20000000, 'Checking', 'Good', 1113),
    (3351, 90000000, 'Investing', 'Frozen', 1114);

-- Insert statements for the Transaction table
INSERT INTO Transaction(TransAmount, TransType, TransDate, AccID, CustomerID)
VALUES
    (2.69, 'FOOD', '2020-01-01', 1234, 1111),
    (100000, 'BMW M3 COMP', '2024-01-01', 4321, 1112),
    (5000312, 'PENTHOUSE', '1999-12-28', 6222, 1113),
    (170000, 'PORSCHE GT3', '2019-05-24', 3351, 1114);

-- Insert statements for the Loan table
INSERT INTO Loan(LoanAmm, InterestRate, LoanStatus, customerID)
VALUES
    (90000, 6.00, 'ACTIVE', 1111),
    (1000000, 0.05, 'GRACE', 1112),
    (50000, 4.00, 'REPAYMENT', 1113),
    (100000, 4.00, 'GRACE', 1114);
