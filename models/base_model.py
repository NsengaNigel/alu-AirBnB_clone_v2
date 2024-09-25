#!/usr/bin/python3
"""BaseModel Module."""

from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
import models

Base = declarative_base()


class BaseModel:
    """Base class for all models."""

    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance."""
        if kwargs:
            for key, value in kwargs.items():
                if key != "_sa_instance_state":
                    setattr(self, key, value)

    def save(self):
        """Save the current instance to the storage."""
        models.storage.new(self)
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """Convert the instance into a dictionary."""
        obj_dict = self.__dict__.copy()
        obj_dict.pop('_sa_instance_state', None)
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def delete(self):
        """Delete the current instance from the storage."""
        models.storage.delete(self)
