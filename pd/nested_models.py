from typing import List
from pydantic import BaseModel, Field

# We can reuse the Product model from the previous example
class Product(BaseModel):
    product_id: str = Field(pattern=r'^prod-\d{4}$')
    name: str = Field(max_length=50)
    price: float = Field(gt=0)
    stock: int = Field(ge=0, default=0)


class Order(BaseModel):
    order_id: int
    customer_name: str
    # The `products` field is a list where each item must match the Product model
    products: List[Product]


# Let's create an order from raw dictionary data
order_data = {
    'order_id': 555,
    'customer_name': 'Jane Doe',
    'products': [
        {'product_id': 'prod-1111', 'name': 'Super Widget', 'price': 99.99},
        {'product_id': 'prod-2222', 'name': 'Mega Gizmo', 'price': 149.50, 'stock': 10}
    ]
}

# Pydantic recursively validates and creates the nested objects
order = Order(**order_data)

print(order)
# You can now access nested data with dot notation
print(f"First product name: {order.products[0].name}")
#> First product name: Super Widget


# Export to a dictionary
order_dict = order.model_dump()
print(f"Order as dict:\n{order_dict}")

print("-" * 20)

# Export to a JSON string with nice formatting
order_json = order.model_dump_json(indent=2)
print(f"Order as JSON:\n{order_json}")
