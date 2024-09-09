#!/usr/bin/python3
"""define delivery structure"""
from models.base_model import Base_model, Base
from sqlalchemy  import Column, String, ForeignKey


class Delivery(Base_model, Base):
    """define delivery attributes"""
    
    __tablename__ = "deliveries"
    user_id = Column(String(60), nullable=False)
    order_id = Column(String(60), ForeignKey('orders.id', ondelete='CASCADE'), nullable=False)
    order_status = Column(String(120), default="In Progress")
