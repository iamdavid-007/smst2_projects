import copy
import typing
from fastapi import HTTPException
from schema.product_schema import Product, products
from logger import logger

from schema.order_schema import OrderCreate, Order


class OrderService:

    @staticmethod
    def order_parser(orders: list[Order]):
        clone_order = copy.deepcopy(orders)

        for order in clone_order:
            order_items = order.items
            new_order = []
            for product_id in order_items: 
                product = products.get(product_id)
                new_order.append(product)
            order.items = new_order
        return clone_order

    @staticmethod
    def check_availability(payload: OrderCreate):
        product_ids = payload.items
        for product_id in product_ids:
            product: Product = products.get(int(product_id))
            if product.quantity_available < 1:
                logger.warning(f"Product not available")
                raise HTTPException(status_code=400, detail="Product not available")
            product.quantity_available -= 1
        return payload

    
order_service = OrderService()
