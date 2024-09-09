#!/usr/bin/python3
"""Base of all model classes all models will inherit from base_model"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from datetime import datetime
import models
import uuid

Base = declarative_base()

time_format = "%Y-%m-%dT%H:%M:%S.%f"

class Base_model():
    """Mother models."""

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
    

    def __init__(self, **kwargs):
        """Initialize base attributes."""

        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
            if kwargs.get("created_at", None) and type("created_at") is str:
                self.created_at = datetime.strptime(self.created_at, time_format)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type("updated_at") is str:
                self.updated_at = datetime.strptime(self.updated_at, time_format)
            else:
                self.updated_at = datetime.utcnow()

            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = uuid.uuid4()
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def save(self):
        """Add model to storage"""

        self.updated_at = datetime.utcnow()
        print("saving...")
        models.storage.new(self)
        models.storage.save()

    def __str__(self):
        """Display a string representation of a specific object"""

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    def to_dict(self):
        """Create a dictionary of an instances attributes"""

        new_dict = self.__dict__
        if 'created_at' in new_dict and type(new_dict['created_at']) is not str:
            new_dict['created_at'] = new_dict['created_at'].strftime(time_format)
        if 'updated_at' in new_dict and type(new_dict['updated_at']) is not str:
            new_dict['updated_at'] = new_dict['updated_at'].strftime(time_format)
        if '_sa_instance_state' in new_dict:
            del new_dict['_sa_instance_state']
        return new_dict

    def delete(self):
        """DELETE an object from storage."""

        print("good bye")
        models.storage.delete(self)
