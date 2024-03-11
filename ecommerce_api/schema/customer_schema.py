from pydantic import BaseModel 


class Customer(BaseModel):
    id: int
    username: str
    address: str


class CustomerCreate(BaseModel):
    username: str
    address: str


customers: list[Customer] = [
    Customer(id=1, username="damilola", address="shagari road"),
    Customer(id=2, username="kayode", address="22 molete str"),
    Customer(id=3, username="danielle", address="99 john street")
]
