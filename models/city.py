#!/usr/bin/python3
"""City model"""

from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class City(BaseModel):
    """City model"""
    __tablename__ = 'cities'

    # ... existing attributes ...

    places = relationship('Place', backref='city', cascade='all, delete-orphan')
