#!/usr/bin/python3
""" class User inherited from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
	""" Public class attributes """
	email: ""
    password: ""
    first_name: ""
    last_name: ""

	
