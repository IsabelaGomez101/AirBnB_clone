#!/usr/bin/python3
"""
Class that inherit
from BaseModel
"""
from base_model import BaseModel

class Review(BaseModel):
	"""public class attributes"""
    place_id = None
    user_id = None
    text = None