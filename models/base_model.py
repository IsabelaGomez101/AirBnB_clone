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
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id , self.__dict__))
    
    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        dic = self.__dict__
        dic["__class__"] = self.__class__.__name__
        dic["updated_at"] = self.updated_at.isoformat()
        dic["created_at"] = self.created_at.isoformat()
        return dic
