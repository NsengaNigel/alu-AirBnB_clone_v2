#!/usr/bin/python3
"""User class module for AirBnB clone."""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """Represents a user for the AirBnB clone."""
    
    __tablename__ = 'users'
    
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    places = relationship("Place", back_populates="user", cascade="all, delete-orphan")
