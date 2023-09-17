#!/usr/bin/python3
"""
Console module for the HBNB project.
"""

import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program with EOF (Ctrl+D)"""
        print()
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print the id."""
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(arg)()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Print the string representation of an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            try:
                class_name = args[0]
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    instance_id = args[1]
                    key = "{}.{}".format(class_name, instance_id)
                    all_objs = storage.all()
                    if key in all_objs:
                        print(all_objs[key])
                    else:
                        print("** no instance found **")
            except NameError:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            try:
                class_name = args[0]
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    instance_id = args[1]
                    key = "{}.{}".format(class_name, instance_id)
                    all_objs = storage.all()
                    if key in all_objs:
                        del all_objs[key]
                        storage.save()
                    else:
                        print("** no instance found **")
            except NameError:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """Print all string representations of instances."""
        args = arg.split()
        all_objs = storage.all()
        if not args:
            print([str(v) for v in all_objs.values()])
        else:
            try:
                class_name = args[0]
                if class_name in BaseModel.__subclasses__():
                    print([str(v) for k, v in all_objs.items() if class_name in k])
                else:
                    print("** class doesn't exist **")
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance attribute."""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            try:
                class_name = args[0]
                if class_name in BaseModel.__subclasses__():
                    if len(args) < 2:
                        print("** instance id missing **")
                        return
                    instance_id = args[1]
                    key = "{}.{}".format(class_name, instance_id)
                    all_objs = storage.all()
                    if key in all_objs:
                        if len(args) < 3:
                            print("** attribute name missing **")
                            return
                        attribute_name = args[2]
                        if len(args) < 4:
                            print("** value missing **")
                            return
                        attribute_value = args[3]
                        instance = all_objs[key]
                        setattr(instance, attribute_name, attribute_value)
                        instance.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** class doesn't exist **")
            except NameError:
                print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
