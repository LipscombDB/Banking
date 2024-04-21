from core import app
from flask import redirect, request 
from flask.templating import render_template
from models import account, accountInfo

# A decorator used to tell the application 
# which URL is associated with which function 
@app.route('/hello')	 
def hello(): 
	return 'HELLO'

# APP ROUTE TO GET RESULTS FOR SELECT QUERY 
@app.route('/get_accounts', methods=['GET','POST']) 
def get_results(): 
    accounts = account.get_accounts()  
    return accounts 

# APP ROUTE TO RENDER HOME PAGE WITH LIST OF accountS
@app.route('/')
def index():
	# Query all data and then pass it to the template
	accounts = account.get_accounts()
	return render_template('index.html', accounts=accounts)

# APP ROUTE TO RENDER FORM TO ADD account DATA
@app.route('/add_data')
def add_data():
	return render_template('add_account.html')

# APP ROUTE TO CALL FUNCTION TO ADD account
@app.route('/add', methods=["POST"])
def add_account():
	
	# In this function we will input data from the 
	# form page and store it in our database.
	# Remember that inside the get the name should
	# exactly be the same as that in the html
	# input fields
	first_name = request.form.get("first_name")
	last_name = request.form.get("last_name")

	# call model function that will store data as a row in our datatable
	if first_name != '' and last_name != '':
		account.add_account(first_name, last_name)
		return redirect('/')
	else:
		return redirect('/')

# APP ROUTE TO CALL FUNCTION TO DELETE account
@app.route('/delete/<int:id>')
def delete_account(id):
	# Deletes the data on the basis of unique id and 
	# redirects to home page
	account.delete_account(id)
	return redirect('/')

# APP ROUTE TO CALL FUNCTION TO RETRIEVE AND RETURN account INFO
@app.route('/account_info')
def get_account_info():
	return accountInfo.get_account_info()

if __name__=='__main__': 
    app.run(port=8000, debug=True) 


