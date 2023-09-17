#!/usr/bin/python3
"""
Console module for the HBNB project.
"""

import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing on an empty line"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program with EOF (Ctrl+D)"""
        print()
        return True

    def do_create(self, arg):
        """Create a new instance of BaseModel and save it"""
        if not arg:
            print("** class name missing **")
        else:
            try:
                new_instance = BaseModel()
                new_instance.save()
                print(new_instance.id)
            except Exception as e:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                instance_id = args[1]
                key = class_name + "." + instance_id
                instances = storage.all()
                if key in instances:
                    print(instances[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                instance_id = args[1]
                key = class_name + "." + instance_id
                instances = storage.all()
                if key in instances:
                    del instances[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of instances"""
        args = arg.split()
        instances = storage.all()
        if not args:
            print([str(instance) for instance in instances.values()])
        else:
            class_name = args[0]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
            else:
                print([str(instance) for key, instance in instances.items() if key.startswith(class_name + ".")])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                instance_id = args[1]
                key = class_name + "." + instance_id
                instances = storage.all()
                if key not in instances:
                    print("** no instance found **")
                elif len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    attribute_name = args[2]
                    attribute_value = args[3]
                    instance = instances[key]
                    setattr(instance, attribute_name, attribute_value)
                    instance.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
