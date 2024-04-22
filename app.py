from core import app
from flask import redirect, request
from flask.templating import render_template
from models import Account,Customer,Transaction,Loans

@app.route('/hello')	 
def hello(): 
    return 'HELLO'

# Route to get all accounts
@app.route('/get_accounts', methods=['GET']) 
def get_results_accounts(): 
    accounts = Account.get_accounts()  
    return render_template('accounts.html', accounts=accounts)

# Route to get all customers
@app.route('/get_customers', methods=['GET'])
def get_results_customers():
    customers = Customer.get_customers()
    return render_template('customers.html', customers=customers)

# Route to get all transactions
@app.route('/get_transactions', methods=['GET'])
def get_results_transactions():
    transactions = Transaction.get_transactions()
    return render_template('transactions.html', transactions=transactions)

# Route to get all loans
@app.route('/get_loans', methods=['GET'])
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
        balances = request.form.get("balance")
        acc_type = request.form.get("accType")
        acc_status = request.form.get("accStatus")
        if balances and acc_type and acc_status:
            Account.add_account(balances,acc_type,acc_status)
            return redirect('/get_accounts')
    return render_template('accountadd.html')

@app.route('/delete_account', methods=['GET'])
def delete_account_form():
    accounts = Account.get_accounts()  # Fetch all accounts
    return render_template('accountdelete.html', accounts=accounts)


@app.route('/delete_account', methods=['POST'])
def delete_account_route():
    accountID = request.form.get('accountID')
    if accountID:
        Account.delete_account(int(accountID))
    return redirect('/get_accounts')

# Route to handle the form submission and add a customer
@app.route('/add_customer', methods=['GET','POST'])
def add_customer():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        if first_name and last_name and email:
            Customer.add_customer(first_name, last_name, email)
            return redirect('/get_customers')
    return render_template('customeradd.html')

@app.route('/delete_customer', methods=['GET'])
def render_delete_customer_form():
    customers = Customer.get_customers()
    return render_template('customerdelete.html', customers=customers)

@app.route('/delete_customer', methods=['POST'])
def delete_customer():
    customer_id = request.form.get('customer_id')
    if customer_id:
        Customer.delete_customer(int(customer_id))
    return redirect('/get_customers')

@app.route('/transaction_add', methods=['GET','POST'])
def add_transaction():
    if request.method == 'POST':
        trans_amount = request.form.get('trans_amount')
        trans_type = request.form.get('trans_type')
        trans_date = request.form.get('trans_date')
        acc_id = request.form.get('acc_id')
        customer_id = request.form.get('customer_id')
        
        if trans_amount and trans_type and trans_date and acc_id and customer_id:
            Transaction.add_transaction(trans_amount, trans_type, trans_date, acc_id, customer_id)
            return redirect('/get_transactions')
    
    return render_template('transactionadd.html')

@app.route('/transaction_delete_form', methods=['GET'])
def delete_transaction_form():
    transactions = Transaction.get_transactions()
    return render_template('transactiondelete.html', transactions=transactions)


@app.route('/transaction_delete', methods=['GET', 'POST'])
def delete_transaction():
    if request.method == 'POST':
        transaction_id = request.form.get('transaction_id')
        if transaction_id:
            Transaction.delete_transaction(int(transaction_id))
            return redirect('/get_transactions')
    
    return render_template('transactiondelete.html')


@app.route('/add_loan', methods=['GET', 'POST'])
def add_loan():
    if request.method == 'POST':
        loan_amount = request.form.get('loan_amount')
        interest_rate = request.form.get('interest_rate')
        loan_status = request.form.get('loan_status')
        customer_id = request.form.get('customer_id')

        if loan_amount and interest_rate and loan_status and customer_id:
            Loans.add_loan(loan_amount, interest_rate, loan_status, customer_id)
            return redirect('/get_loans')

    return render_template('add_loan.html')


@app.route('/delete_loan_form', methods=['GET'])
def delete_loan_form():
    loans = Loans.get_loans()
    return render_template('delete_loan.html', loans=loans)

@app.route('/delete_loan', methods=['POST'])
def delete_loan():
    if request.method == 'POST':
        loan_id = request.form.get('loan_id')
        if loan_id:
            Loans.delete_loan(int(loan_id))
            return redirect('/get_loans')

    return render_template('delete_loan.html')



    



# Additional routes for adding, updating, deleting for Customer, Transaction, Loan can be created similarly

if __name__ == '__main__': 
    app.run(port=8000, debug=True)