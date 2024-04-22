
from models.schemas import Loan
from core import ma, db

def get_loans(): 
    all_loans = Loan.query.all()
    return loans_schema.dump(all_loans)

def add_loan(loan_amount, interest_rate, loan_status, customer_id):
    new_loan = Loan(
        LoanAmount=loan_amount, 
        InterestRate=interest_rate, 
        LoanStatus=loan_status, 
        CustomerID=customer_id
    )
    db.session.add(new_loan)
    db.session.commit()

def delete_loan(id):
    loan = Loan.query.get(id)
    db.session.delete(loan)
    db.session.commit()
     
class LoanSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Loan
        load_instance = True

loan_schema = LoanSchema()
loans_schema = LoanSchema(many=True)
