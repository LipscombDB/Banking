
from models.schemas import Transaction
from core import ma, db

def get_transactions(): 
    all_transactions = Transaction.query.all()
    return transactions_schema.dump(all_transactions)

def add_transaction(trans_amount, trans_type, trans_date, acc_id, customer_id):
    new_transaction = Transaction(
        TransAmount=trans_amount, 
        TransType=trans_type, 
        TransDate=trans_date,
        AccID=acc_id, 
        CustomerID=customer_id
    )
    db.session.add(new_transaction)
    db.session.commit()

def delete_transaction(id):
    transaction = Transaction.query.get(id)
    db.session.delete(transaction)
    db.session.commit()
     
class TransactionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Transaction
        load_instance = True

transaction_schema = TransactionSchema()
transactions_schema = TransactionSchema(many=True)