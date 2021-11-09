#!/usr/bin/python3
"""defines all common attributes/methods
for other classes"""
import uuid
import datetime

class BaseModel():
    
    def __init__(self, id=None, created_at=None, updated_at=None):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        print("[{}] ({}) {}".format(self.__class__.__name__, self.id , self.__dict__))

    def save(self):
        self.updated_at = datetime.datetime.now()
    
    def to_dict(self):
        