from fastapi import HTTPException
from schema.customer_schema import CustomerCreate, customers


class CustomerService:
    
    @staticmethod
    def check_unique_username(payload: CustomerCreate):
        for customer in customers:
            if customer.username == payload.username:
                raise HTTPException(status_code=400, detail="Username already exists")
