from fastapi import APIRouter, HTTPException
from schema.product_schema import ProductCreate, products, Product

product_router = APIRouter()

# Create a new product
# List products
# Edit product


# Create a new product
@product_router.post("/", status_code=201)
def create_product(payload: ProductCreate):
    # Get product ID
    product_id = len(products) + 1
    new_product = Product(
        id=product_id,
        name=payload.name,
        price=payload.price,
        quantity_available=payload.quantity_available
    )
    products[product_id] = new_product
    return {"message": "Product created successfully", "data": new_product}


# List products
@product_router.get("/", status_code=200)
def list_products():
    return {"message": "List of products", "data": products}

# Edit a product


@product_router.put("/{product_id}", status_code=200)
def edit_product(product_id: int, payload: ProductCreate):
    if product_id not in products:
        raise HTTPException(status_code=404, detail="Product not found")
    current_product = products[product_id]
    current_product.name = payload.name
    current_product.price = payload.price
    current_product.quantity_available = payload.quantity_available
    return {"message": "Product updated successfully", "data": current_product}
