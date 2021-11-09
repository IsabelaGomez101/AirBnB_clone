#!/usr/bin/python3
""" program called console.py that contains 
entry point of the command interpreter """
import cmd
import json
import sys
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb)"
    
    def do_create(self, class_name):
        """ create [class_name]
        Creates a new instance of BaseModel """
        list_classes = {'BaseModel': 'BaseModel'}
        if class_name:
            if class_name == "BaseModel":
                obj = BaseModel()
                print(obj.id)
                print("exist")
            else:
               print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_EOF(self, line):
        """ EOF command to exit the program """
        return True

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()