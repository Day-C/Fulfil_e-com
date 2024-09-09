#!/usr/bin/python3
"""Define brend structure."""
from models.base_model import Base_model, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship



class Brand(Base_model, Base):
    """brand attrs"""

    __tablename__ = "brands"
    name = Column(String(60), nullable=False)
    subcategory_id = Column(String(60), ForeignKey("subcategories.id", ondelete='CASCADE'), nullable=False)
    products = relationship("Product", backref="brand_name")
