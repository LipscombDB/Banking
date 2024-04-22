from models.schemas import Account
from core import ma, db

def get_accounts(): 
    all_accounts = Account.query.all()
    return accounts_schema.dump(all_accounts)

def add_account(balances, acc_type, acc_status):
    new_account = Account(Balances=balances, AccType=acc_type, AccStatus=acc_status)
    db.session.add(new_account)
    db.session.commit()

def delete_account(id):
    account = Account.query.get(id)
    db.session.delete(account)
    db.session.commit()

class AccountSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Account
        load_instance = True

account_schema = AccountSchema()
accounts_schema = AccountSchema(many=True)
