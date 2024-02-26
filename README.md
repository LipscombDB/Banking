# Banking

## Requests
### Customer request bank account balance
SELECT Customer.FirstName, Accounts.Balances
FROM Accounts
JOIN Customers ON Account.CustomerID = Customer.CustomerId
WHERE Customers.CustomerID = '1234','4321';


### Customer request loan amount 

### Business request Customer ID

### Business request Customer Account Status
