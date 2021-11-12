#!/usr/bin/python3
""" program called console.py that contains 
entry point of the command interpreter """
import cmd
import json
import sys
import shlex
from models.base_model import BaseModel
from models.__init__ import storage
list_classes = ['BaseModel']

class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb)"
    
    def do_create(self, class_name):
        """ create [class_name]
        Creates a new instance of BaseModel """
        if class_name:
            if class_name in list_classes:
                obj = eval('{}()'.format(class_name))
                obj.save()
                print(obj.id)
            else:
               print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, argv):
        objs = storage.all()
        args = argv.split(" ")
        if args[0]:
            if args[0] in list_classes:
                if args[1]:
                    k = args[0] + "." + args[1]
                    if k in objs.keys():
                        for key, value in objs.items():
                            if k == key:
                                print(value.__str__())
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
    
    """ def do_destroy(self, argv):
        args = argv.split(" ")
        if args[0]:
            if args[0] == "BaseModel"
                if args[1]:
                    if id is args[0]:  """
                        
    def do_all(self, name):
        objs = storage.all()
        list_obj = []
        if name in list_classes:
            for key, value in objs.items():
                if objs[key].__class__.__name__ == name:
                    list_obj.append(value.__str__())   
        else:
            for key, value in objs.items():
                list_obj.append(value.__str__())
        print(list_obj)
    
    def do_destroy(self, argv):
        objs = storage.all()
        args = argv.split(" ")
        if args[0]:
            if args[0] in list_classes:
                if args[1]:
                    k = args[0] + "." + args[1]
                    if k in objs.keys():
                        for key in objs.keys():
                            if k == key:
                                objs.pop(k)
                                storage.save()
                                break
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_update(self, argv):
        objs = storage.all()
        args = shlex.split(argv)
        if args[0]:
            if args[0] in list_classes:
                if args[1]:
                    k = args[0] + "." + args[1]
                    if k in objs.keys():
                        if args[2]:
                            if args[3]:
                                for key, value in objs.items():
                                    if k == key:
                                        setattr(value, args[2], args[3])
                                        print(value.to_dict())
                                        storage.save()
                                        break
                            else:
                                print("** value missing **")
                        else:
                            print("** attribute name missing **") 
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
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