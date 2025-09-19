from pydantic import BaseModel, Field, ValidationError

class Product(BaseModel):
    # Apply constraints to each field
    product_id: str = Field(pattern=r'^prod-\d{4}$') # e.g., prod-1234
    name: str = Field(max_length=50)
    price: float = Field(gt=0) # Price must be greater than 0
    stock: int = Field(ge=0, default=0) # Stock must be >= 0

# A valid product
valid_product = Product(
    product_id='prod-9876',
    name='Super Widget',
    price=99.99
)
print(f"Valid Product: {valid_product}")
#> Valid Product: product_id='prod-9876' name='Super Widget' price=99.99 stock=0

print("-" * 20)

# An invalid product
try:
    Product(product_id='wrong-format', name='Gadget', price=-10.0)
except ValidationError as e:
    print(e)
    """
    #> 2 validation errors for Product
    #> product_id
    #>   String should match pattern '^prod-\d{4}$' [type=string_pattern_mismatch, ...
    #> price
    #>   Input should be greater than 0 [type=greater_than, ...
    """