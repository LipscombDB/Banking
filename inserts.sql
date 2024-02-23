INSERT INTO Customer(FirstName, LastName, Email, AccountID  )
VALUES
(
    'Spongebob', 'Squarepants', 'spsqaurepants@bikinibottom.com','1234' 
)

(
    'Patrick', 'Star', 'patstar@bikinibottom.com','4321' 
)

(
    'Lewis','Hamilton','benzbetter@mercedes.com','6222'
)

(
    'Max', 'Verstappen', 'maxverstappen@redbull.com','3351' 
)

INSERT INTO Account(accountID, Balances, AccTypes,AccStatus,CustomerID)
VALUES 
(
'1234','0','Checking','Frozen','1111'
)
(
'4321','100000000','Savings', 'Good', '1112'
)
(
'6222', '20000000','Checking', 'Good', '1113'
)
(
'3351', '90000000', 'Investing', 'Frozen', '1114'
)

INSERT INTO Transaction(TransactionID, TransAmount, TransType, TransDate, AccID, CustomerID)
(
    '9999','2.69','FOOD','2020-1-1','1234','1111'
)
(
    '9998','100,000','BMW M3 COMP','2024-1-1','4321','1112'
)
(
    '9997','5,000,312','PENTHOUSE','1999-12-28','6222','1113'
)
(
    '9996','170,000','PORSCHE GT3','2019-5-24','3351','1114'
)

INSERT INTO Loan(LoanID,LoanAmm,InterestRate,LoanStatus,customerID,AccID)
(
    '5555','90,000','6%','1111','1234'
)
