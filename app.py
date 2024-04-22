from core import app
from flask import redirect, request
from flask.templating import render_template
from models import Account,Customer,Transaction,Loans

@app.route('/hello')	 
def hello(): 
    return 'HELLO'

# Route to get all accounts
@app.route('/get_accounts', methods=['GET', 'POST']) 
def get_results_accounts(): 
    accounts = Account.get_accounts()  
    return render_template('accounts.html', accounts=accounts)

# Route to get all customers
@app.route('/get_customers', methods=['GET', 'POST'])
def get_results_customers():
    customers = Account.get_customers()
    return render_template('customers.html', customers=customers)

# Route to get all transactions
@app.route('/get_transactions', methods=['GET', 'POST'])
def get_results_transactions():
    transactions = Transaction.get_transactions()
    return render_template('transactions.html', transactions=transactions)

# Route to get all loans
@app.route('/get_loans', methods=['GET', 'POST'])
def get_results_loans():
    loans = Loans.get_loans()
    return render_template('loans.html', loans=loans)

# Route to render home page with list of accounts
@app.route('/')
def index():
    accounts = Account.get_accounts()
    return render_template('index.html', accounts=accounts)

# Route to render form to add account data
@app.route('/add_account', methods=["GET", "POST"])
def add_data():
    if request.method == "POST":
        balances = request.form.get("balances")
        acc_type = request.form.get("acc_type")
        acc_status = request.form.get("acc_status")
        if balances and acc_type and acc_status:
            add_account(balances, acc_type, acc_status)
            return redirect('/')
    return render_template('add_account.html')

# Route to delete an account
@app.route('/delete_account/<int:id>')
def delete_account_route(id):
    Account.delete_account(id)
    return redirect('/')

# Additional routes for adding, updating, deleting for Customer, Transaction, Loan can be created similarly

if __name__ == '__main__': 
    app.run(port=8000, debug=True)