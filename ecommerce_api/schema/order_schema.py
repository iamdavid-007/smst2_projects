from pydantic import BaseModel
from typing import Union
from schema.product_schema import Product
from schema.customer_schema import Customer


class Order(BaseModel):
    id: int
    customer_id: Union[int, Customer]
    items: list[int]
    status: str = "pending"


class OrderCreate(BaseModel):
    customer_id: int
    items: list[int]


orders = [
    Order(id=1, customer_id=1, items=[1, 2])
]
