#!/usr/bin/python3
"""defines all common attributes/methods
for other classes"""
import uuid
import datetime
from models.__init__ import storage

class BaseModel():
    
    def __init__(self, *args, **kwargs):
        """ Constructor """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                else:
                    if key == "created_at" or key == "updated_at":
                        value = datetime.datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        """ Method that print a string"""
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id , self.__dict__))
    
    def save(self):
        """ Updates the public instance attribute updated_at """
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__ of the instance """
        dic = self.__dict__
        dic["__class__"] = self.__class__.__name__
        dic["updated_at"] = self.updated_at.isoformat()
        dic["created_at"] = self.created_at.isoformat()
        return dic
