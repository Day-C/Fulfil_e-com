#!/usr/bin/python3
"""define users class"""
from models.base_model import Base_model, Base
from sqlalchemy import Column, String, Integer


class User(Base_model, Base):
    """user inherits from base_model and Base"""

    __tablename__  = "users"
    name = Column(String(60), nullable=False)
    phone_number = Column(Integer, nullable=False)
    email = Column(String(82), nullable=False)
    password = Column(String(30), nullable=False)
    busines_name = Column(String(120), nullable=True)
