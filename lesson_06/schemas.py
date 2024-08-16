from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional
from datetime import datetime

# Схемы для пользователей


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int

    class Config:
        model_config = {"from_attributes": True}


# Схемы для товаров


class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float


class ProductCreate(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: int

    class Config:
        model_config = {"from_attributes": True}


# Схемы для заказов


class OrderBase(BaseModel):
    user_id: int
    product_id: int
    order_date: datetime
    status: str


class OrderCreate(OrderBase):
    pass


class OrderResponse(OrderBase):
    id: int

    class Config:
        model_config = {"from_attributes": True}
