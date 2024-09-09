#/usr/bin/python3
"""Define address structure"""
from models.base_model import Base_model, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Subcategory(Base_model, Base):
    """define address attributes"""

    __tablename__ = "subcategories"
    category_id = Column(String(60), ForeignKey("categories.id", ondelete='CASCADE'), nullable=False)
    name = Column(String(82), nullable=False)
    products = relationship('Product', backref="subcategory")
