from pydantic import BaseModel, ValidationError

# 1. Define the data shape by inheriting from BaseModel
class User(BaseModel):
    id: int
    name: str
    is_active: bool = True # You can provide default values

# 2. Instantiate with valid data
# Pydantic will automatically convert types where possible (e.g., '123' -> 123)
user_data = {'id': '123', 'name': 'Alex'}
user = User(**user_data)

print(user)
#> id=123 name='Alex' is_active=True
print(f"User ID is an integer: {isinstance(user.id, int)}")
#> User ID is an integer: True

print("-" * 20)

# 3. Instantiate with invalid data
# This will raise a `ValidationError`
invalid_user_data = {'id': 'abc', 'name': 'Bob'}
try:
    invalid_user = User(**invalid_user_data)
except ValidationError as e:
    print(e)
    """
    #> 1 validation error for User
    #> id
    #>   Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='abc', input_type=str]
    """

