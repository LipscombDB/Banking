
from models.schemas import Transaction  # Adjust this import according to your actual module structure
from core import ma, db

def get_transactions(): 
    all_transactions = Transaction.query.all()
    return transactions_schema.dump(all_transactions)

def add_transaction(trans_amount, trans_type, acc_id, customer_id):
    new_transaction = Transaction(
        TransAmount=trans_amount, 
        TransType=trans_type, 
        TransDate=func.now(),  # Automatically set the transaction date to now
        AccID=acc_id, 
        CustomerID=customer_id
    )
    db.session.add(new_transaction)
    db.session.commit()

def delete_transaction(id):
    # Deletes the transaction based on the unique TransactionID
    transaction = Transaction.query.get(id)
    db.session.delete(transaction)
    db.session.commit()
     
class TransactionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Transaction
        load_instance = True  # Optional: Allows for model instances to be automatically loaded

transaction_schema = TransactionSchema()
transactions_schema = TransactionSchema(many=True)