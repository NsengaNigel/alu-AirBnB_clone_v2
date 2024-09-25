#!/usr/bin/python3
""" Module for Place class """
from models.base_model import BaseModel
from models.base import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


place_amenity = Base.metadata.tables['place_amenity']

class Place(BaseModel, Base):
    """ Place class for storage in database """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(int, default=0)
    number_bathrooms = Column(int, default=0)
    max_guest = Column(int, default=0)
    price_by_night = Column(int, default=0)
    latitude = Column(float, nullable=True)
    longitude = Column(float, nullable=True)

    amenities = relationship("Amenity", secondary="place_amenity", viewonly=False, back_populates="place_amenities")

    @property
    def amenities(self):
        """ Getter for amenities attribute """
        return [Amenity.get(id) for id in self.amenity_ids]

    @amenities.setter
    def amenities(self, amenity):
        """ Setter for amenities attribute """
        if isinstance(amenity, Amenity):
            self.amenity_ids.append(amenity.id)
