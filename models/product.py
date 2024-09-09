#!/usr/bin/python3
"""define product class"""
from models.base_model import Base_model, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey


class Product(Base_model, Base):
    """product model"""

    __tablename__ = "products"
    name = Column(String(50), nullable=False)
    price = Column(Integer, nullable=False)
    sub_ategory = Column(String(60), ForeignKey('subcategories.id', ondelete='CASCADE'), nullable=True)
    brand = Column(String(60), ForeignKey('brands.id', ondelete='CASCADE'), nullable=True)
    order_id = Column(String(60), ForeignKey("orders.id", ondelete='CASCADE'), nullable=True)
    weight = Column(Float, nullable=True)
    img_url = Column(String(120), nullable=False)
