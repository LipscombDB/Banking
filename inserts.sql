-- Inserting into Account table
INSERT INTO Account (Balances, AccType, AccStatus) 
VALUES 
(1000.00, 'Savings', 'Active'),
(500.00, 'Checking', 'Active'),
(2000.00, 'Savings', 'Active');

-- Inserting into Customer table
INSERT INTO Customer (FName, LName, email) 
VALUES 
('John', 'Doe', 'john.doe@example.com'),
('Jane', 'Smith', 'jane.smith@example.com'),
('Alice', 'Johnson', 'alice.johnson@example.com');

-- Inserting into Transaction table
INSERT INTO Transaction (TransAmount, TransType, TransDate, AccID, CustomerID) 
VALUES 
(100.00, 'Deposit', '2024-04-16 10:00:00', 1, 1),
(50.00, 'Withdrawal', '2024-04-16 11:00:00', 2, 2),
(200.00, 'Deposit', '2024-04-16 12:00:00', 3, 3);

-- Inserting into Loan table
INSERT INTO Loan (LoanAmount, InterestRate, LoanStatus, CustomerID) 
VALUES 
(5000.00, 0.05, 'Active', 1),
(3000.00, 0.04, 'Active', 2),
(7000.00, 0.06, 'Active', 3);
