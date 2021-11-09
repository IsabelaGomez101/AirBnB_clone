#!/usr/bin/python3
import json

class FileStorage():
    """Private class attributes"""
    __file_path = "filename"
    __objects = {}

    def all(self):
        return FileStorage.__objects
    
    def new(self, obj):
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj
        
    def save(self):
        with open ("filename", 'w') as f:
            s = (json.dumps(FileStorage.__objects))
            f.write(s)

    def reload(self):
        if FileStorage.__file_path:
            with open (FileStorage.__file_path, 'r') as f:
                return json.load(f)
        else: 
            pass
    

    
