#!/usr/bin/python3
"""User model"""

from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class User(BaseModel):
    """User model"""
    __tablename__ = 'users'

    # ... existing attributes ...

    places = relationship('Place', backref='user', cascade='all, delete-orphan')
