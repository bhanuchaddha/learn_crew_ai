from datetime import date
from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class ShoppingCartItem(BaseModel):
    product_id: int
    quantity: int

class Customer(BaseModel):
    customer_id: int
    first_name: str
    last_name: str
    email: str
    phone: str
    address: Address
    joined_date: date
    shopping_cart: List[ShoppingCartItem] = []

class Product(BaseModel):
    product_id: int
    product_name: str
    category: str
    price: float
    stock: int
    description: str

class CustomerAndProductData(BaseModel):
    customers: List[Customer]
    products: List[Product]

class Customers(BaseModel):
    customers: List[Customer]

class Products(BaseModel):
    products: List[Product]