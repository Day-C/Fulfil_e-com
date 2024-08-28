#!/usr/bin/python3
"""Define orders class"""
from sqlalchemy.orm import relationship
from models.base_model import Base_model, Base
from sqlalchemy import Column, String, ForeignKey


class Order(Base_model, Base):
    """define order attributes."""

    __tablename__ = "orders"
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    products = relationship("Product", backref="order")
    order_status = Column(String(20), default="not_approved")
