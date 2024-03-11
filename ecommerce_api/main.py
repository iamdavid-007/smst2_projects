from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware
from routers.customer import customer_router
from routers.product import product_router
from routers.order import order_router
from middleware import ecommerce_middleware
from idlelib.debugobj import dispatch
from logger import logger
app = FastAPI()
logger.info("===Starting App===")

app.include_router(customer_router, prefix="/customer", tags=["customer"])
app.include_router(product_router, prefix="/product", tags=["product"])
app.include_router(order_router, prefix="/order", tags=["order"])
app.add_middleware(BaseHTTPMiddleware, dispatch=ecommerce_middleware)

customers = [
    {
        "name": "John",
        "age": 25,
        "phone": "1234567890"
    },
    {
        "name": "Doe",
        "age": 30,
        "phone": "1234567890"
    },
    {
        "name": "Smith",
        "age": 35,
        "phone": "1234567890"
    }
]


@app.get("/welcome")
def index():
    return {"message": "welcome to our store"}


@app.get("/customers")
def get_customers():
    return {"message": "success", "data": customers}


@app.post("/customers")
def create_customer(name, age, phone):
    customer = {
        "name": name,
        "age": age,
        "phone": phone
    }
    customers.append(customer)
    return {"message": "Customer Created Successfully", "data": customer}


@app.put("/customers/{name}")
def update_customer(name, age, phone):
    for customer in customers:
        if customer["name"] == name:
            customer["age"] = age
            customer["phone"] = phone
            return {"message": "Customer Updated Successfully", "data": customer}
  
# GET
# POST
# PUT
# DELETE
