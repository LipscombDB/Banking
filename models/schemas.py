from sqlalchemy import DateTime
from core import db
from sqlalchemy.sql import func

class Account(db.Model):
    accountID = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    Balances = db.Column(db.Numeric(32, 2), nullable=True)
    AccType = db.Column(db.String(10), nullable=True)
    AccStatus = db.Column(db.String(10), nullable=True)

class Customer(db.Model):
    CustomerID = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    FName = db.Column(db.String(50), nullable=True)
    LName = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(50), nullable=True)

class Transaction(db.Model):
    TransactionID = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    TransAmount = db.Column(db.Numeric(32, 2), nullable=True)
    TransType = db.Column(db.String(15), nullable=True)
    TransDate = db.Column(db.DateTime(timezone=True))
    AccID = db.Column(db.Integer, db.ForeignKey('account.accountID'), nullable=True)
    CustomerID = db.Column(db.Integer, db.ForeignKey('customer.CustomerID'), nullable=True)

class Loan(db.Model):
    LoanID = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    LoanAmount = db.Column(db.Numeric(32, 2), nullable=True)
    InterestRate = db.Column(db.Numeric, nullable=True)
    LoanStatus = db.Column(db.String(10), nullable=True)
    CustomerID = db.Column(db.Integer, db.ForeignKey('customer.CustomerID'), nullable=True)