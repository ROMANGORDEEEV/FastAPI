from sqlalchemy.orm import Session
from models import User, Product, Order
from schemas import (
    UserCreate,
    UserResponse,
    ProductCreate,
    ProductResponse,
    OrderCreate,
    OrderResponse,
)
from passlib.context import CryptContext
from typing import List

# Настройка для хэширования паролей
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


# CRUD операции для пользователей


def create_user(db: Session, user: UserCreate) -> UserResponse:
    db_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        password=get_password_hash(user.password),
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return UserResponse.model_validate(db_user)


def get_user(db: Session, user_id: int) -> UserResponse:
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        return UserResponse.model_validate(db_user)
    return None


def get_users(db: Session, skip: int = 0, limit: int = 10) -> List[UserResponse]:
    db_users = db.query(User).offset(skip).limit(limit).all()
    return [UserResponse.model_validate(user) for user in db_users]


def delete_user(db: Session, user_id: int) -> UserResponse:
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return UserResponse.model_validate(db_user)
    return None


# CRUD операции для товаров


def create_product(db: Session, product: ProductCreate) -> ProductResponse:
    db_product = Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return ProductResponse.model_validate(db_product)


def get_product(db: Session, product_id: int) -> ProductResponse:
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product:
        return ProductResponse.model_validate(db_product)
    return None


def get_products(db: Session, skip: int = 0, limit: int = 10) -> List[ProductResponse]:
    db_products = db.query(Product).offset(skip).limit(limit).all()
    return [ProductResponse.model_validate(product) for product in db_products]


def delete_product(db: Session, product_id: int) -> ProductResponse:
    db_product = db.query(Product).filter(Product.id == product_id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return ProductResponse.model_validate(db_product)
    return None


# CRUD операции для заказов


def create_order(db: Session, order: OrderCreate) -> OrderResponse:
    db_order = Order(**order.model_dump())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return OrderResponse.model_validate(db_order)


def get_order(db: Session, order_id: int) -> OrderResponse:
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if db_order:
        return OrderResponse.model_validate(db_order)
    return None


def get_orders(db: Session, skip: int = 0, limit: int = 10) -> List[OrderResponse]:
    db_orders = db.query(Order).offset(skip).limit(limit).all()
    return [OrderResponse.model_validate(order) for order in db_orders]


def delete_order(db: Session, order_id: int) -> OrderResponse:
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if db_order:
        db.delete(db_order)
        db.commit()
        return OrderResponse.model_validate(db_order)
    return None
