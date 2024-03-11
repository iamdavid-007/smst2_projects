from fastapi import APIRouter, Depends
from schema.customer_schema import CustomerCreate, customers, Customer
from fastapi import HTTPException
from services.customer_service import CustomerService

customer_router = APIRouter()

# create an instance of the CustomerService class

customer_service = CustomerService()

# Create a new customer
# List customers
# Edit a customer


# Create a new customer
@customer_router.post("/", status_code=201)
def create_customer(payload: CustomerCreate, check: None=Depends(customer_service.check_unique_username)):
    customer_id = len(customers) + 1
    new_customer = Customer(
        id=customer_id,
        username=payload.username,
        address=payload.address
    )
    customers.append(new_customer)
    return {"message": "Customer created successfully", "data": new_customer}


# List customers
@customer_router.get("/", status_code=200)
def list_customers():
    return {"message": "List of customers", "data": customers}

    
# Edit a customer
@customer_router.put("/{customer_id}", status_code=200)
def edit_customer(customer_id: int, payload: CustomerCreate):
    current_customer = None
    for customer in customers:
        if customer.id == customer_id:
            current_customer = customer
            break
    if not current_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    current_customer.username = payload.username
    current_customer.address = payload.address
    return {"message": "Customer updated successfully", "data": current_customer}
