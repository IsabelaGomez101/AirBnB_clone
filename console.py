#!/usr/bin/python3
""" program called console.py that contains
entry point of the command interpreter """
import cmd
import json
import sys
import shlex
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.city import City
from models.review import Review
from models.state import State
from models.__init__ import storage
list_classes = ['BaseModel', 'User', 'Amenity', 'Place',
                'City', 'Review', 'State']


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb)"

    def do_create(self, class_name):
        """ Creates a new instance of any of these classes:
        ['BaseModel', 'User', 'Amenity', 'Place', 'City', 'Review', 'State']
        Ex: $create BaseModel """
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
        """ Prints the string representation of an instance
        based on the class name and id.
        Ex: $show BaseModel 5500fd26-19a3-436d-b8e5-96f00670e0d4 """
        objs = storage.all()
        args = argv.split(" ")
        if args[0]:
            if args[0] in list_classes:
                if len(args) == 2:
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

    def do_all(self, name):
        """ Prints all string representation of all instances
        based or not on the class name.
        Ex: $all BaseModel or $all """
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
        """Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $destroy BaseModel 5500fd26-19a3-436d-b8e5-96f00670e0d4 """
        objs = storage.all()
        args = argv.split(" ")
        if args[0]:
            if args[0] in list_classes:
                if len(args) == 2:
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
        """ Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        Ex: $update BaseModel 12121212 email "aibnb@mail.com"."""
        objs = storage.all()
        args = shlex.split(argv)
        if len(args) >= 1:
            if args[0] in list_classes:
                if len(args) >= 2:
                    k = args[0] + "." + args[1]
                    if k in objs.keys():
                        if len(args) >= 3:
                            if len(args) == 4:
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
        print("")
        return True

    def do_quit(self, line):
        """ Quit command to exit the program """
        return True

    def emptyline(self):
        """ blank lines"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
