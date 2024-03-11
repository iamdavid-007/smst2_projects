from pydantic import BaseModel
from decimal import Decimal


class Product(BaseModel):
    id: int
    name: str
    price: Decimal
    quantity_available: int


class ProductCreate(BaseModel):
    name: str
    price: Decimal
    quantity_available: int
    

products = {
    1: Product(id=1, name="steam gift card", price=Decimal("150.00"), quantity_available=1),
    2: Product(id=2, name="itunes gift card", price=Decimal("100.00"), quantity_available=19),
    3: Product(id=3, name="amazon gift card", price=Decimal("50.00"), quantity_available=5)
}
