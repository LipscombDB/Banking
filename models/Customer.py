from sqlalchemy import func
from models.schemas import Customer  # Make sure this import matches your actual module structure
from core import ma, db

def get_customers(): 
    all_customers = Customer.query.all()
    return customers_schema.dump(all_customers)

def add_customer(first_name, last_name, email):
    new_customer = Customer(FName=first_name, LName=last_name, email=email)
    db.session.add(new_customer)
    db.session.commit()

def delete_customer(id):
    # Deletes the customer based on the unique CustomerID
    customer = Customer.query.get(id)
    db.session.delete(customer)
    db.session.commit()
     
class CustomerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Customer
        load_instance = True  # Optional: Allows for model instances to be automatically loaded

customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)
