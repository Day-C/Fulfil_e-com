#!/usr/bin/python3
"""define review class"""
from models.base_model import Base_model, Base
#from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey


class Review(Base_model, Base):
    """Define review structure"""

    __tablename__ = "reviews"
    user_id = Column(String(60), ForeignKey("users.id"), nullable=True)
    product_id = Column(String(60), ForeignKey("products.id"), nullable=True)
    text = Column(String(1022), nullable=False)
