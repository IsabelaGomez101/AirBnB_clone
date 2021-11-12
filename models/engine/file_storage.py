#!/usr/bin/python3
"""
Class FileStorage that serializes
instances to a JSON file and deserializes 
JSON file to instances.
"""
import json
from os.path import os
from models.base_model import BaseModel


class FileStorage():
    """Private class attributes"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj
        
    def save(self):
        """Serializes __objects to the JSON file"""
        dic = {}
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
               dic = json.load(f)
            for key, value in FileStorage.__objects.items():
                dic[key] = value.to_dict()
        else:
            for key, value in FileStorage.__objects.items():
                dic[key] = value.to_dict()
        if dic:
            with open(FileStorage.__file_path, 'w') as f:
                json.dump(dic, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                my_dict = json.load(f)
                for key, value in my_dict.items():
                    self.__objects[key] = BaseModel(**value)
        else: 
            pass
        
