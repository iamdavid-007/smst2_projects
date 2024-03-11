from fastapi import APIRouter, Depends, HTTPException
from schema.order_schema import OrderCreate, orders, Order
from services.order_service import order_service
from routers import customer

order_router = APIRouter()

# List all orders
# Create a new order
# checkout order


@order_router.get("/", status_code=200)
def list_orders():
    response = order_service.order_parser(orders)
    return {"message": "List of orders", "data": response}


@order_router.post("/", status_code=201)
def create_order(payload: OrderCreate=Depends(order_service.check_availability)):
    customer_id: int = payload.customer_id
    product_ids: list[int] = payload.items
    # get current order id
    order_id = len(orders) + 1
    new_order = Order(
        id=order_id,
        customer_id=customer_id,
        items=product_ids
    )
    orders.append(new_order)
    return {"message": "Order created successfully", "data": new_order}


@order_router.put("/checkout/{order_id}", status_code=200)
def checkout_order(order_id: int):
    curr_order = next((order for order in orders if order.id == order_id), None)
    if not curr_order:
        raise HTTPException(status_code=404, detail="Order not found")
    curr_order.status = "completed"
    return {"message": "Order checked out successfully", "data": curr_order}
