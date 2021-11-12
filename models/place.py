#!/usr/bin/python3
"""
Class that inherit
from BaseModel
"""
from base_model import BaseModel

class Place (BaseModel):
    """Public class attributes"""
    city_id = None
    user_id = None
    name = None
    description = None
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0
    longitude = 0
    amenity_ids = None