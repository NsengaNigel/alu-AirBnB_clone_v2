#!/usr/bin/python3
"""User Module.

This module defines the User class, which inherits from BaseModel and Base.
It represents a user in the database with attributes for email, password,
first name, and last name.
"""

from sqlalchemy import Column, String
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """User class for users in the database."""

    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    def __init__(self, *args, **kwargs):
        """Initialize a User instance."""
        super().__init__(*args, **kwargs)
