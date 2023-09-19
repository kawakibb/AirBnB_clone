#!/usr/bin/env python3
"""
Console module for the AirBnB project.
"""

import cmd
import sys
import models

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, line):
        """Create a new instance, save it, and print its id."""
        if not line:
            print("** class name missing **")
            return
        try:
            new_instance = models.classes[line]()
            new_instance.save()
            print(new_instance.id)
        except KeyError:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Show the string representation of an instance."""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        try:
            cls = models.classes[args[0]]
        except KeyError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        objects = models.storage.all()
        instance_key = "{}.{}".format(args[0], args[1])
        if instance_key in objects:
            print(objects[instance_key])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """Delete an instance based on the class name and id."""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        try:
            cls = models.classes[args[0]]
        except KeyError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        objects = models.storage.all()
        instance_key = "{}.{}".format(args[0], args[1])
        if instance_key in objects:
            del objects[instance_key]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """Print string representations of all instances."""
        args = line.split()
        objects = models.storage.all()
        if not args:
            print([str(obj) for obj in objects.values()])
        else:
            try:
                cls = models.classes[args[0]]
            except KeyError:
                print("** class doesn't exist **")
                return
            instances = [str(obj) for key, obj in objects.items() if key.startswith(args[0])]
            if instances:
                print(instances)
            else:
                print("[]")

    def do_update(self, line):
        """Update an instance based on the class name and id."""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        try:
            cls = models.classes[args[0]]
        except KeyError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        objects = models.storage.all()
        instance_key = "{}.{}".format(args[0], args[1])
        if instance_key not in objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        instance = objects[instance_key]
        attribute_name = args[2]
        try:
            value = eval(args[3])
        except (SyntaxError, NameError):
            value = args[3]
        setattr(instance, attribute_name, value)
        instance.save()

    def emptyline(self):
        pass

    def do_quit(self, line):
        """Quit command to exit the program."""
        sys.exit(0)

    def do_EOF(self, line):
        """EOF command to exit the program."""
        print()
        sys.exit(0)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
