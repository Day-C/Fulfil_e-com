#!/usr/vin/python3
"""define category structuer."""
from models.base_model import Base_model, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class Category(Base_model, Base):
    """Define category attrs"""

    __tablename__ = "categories"
    name = Column(String(120), nullable=False)
    description = Column(String(900), nullable=False)
    sub_categories = relationship('Subcategory', backref="category")
