#!/usr/bin/python3
import cmd
import sys
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, line):
        """Create a new instance of BaseModel, saves it (to the JSON file),
        and prints the id. Ex: $ create BaseModel
        """
        if not line:
            print("** class name missing **")
        elif line not in ["BaseModel"]:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on the
        class name and id. Ex: $ show BaseModel 1234-1234-1234.
        """
        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            obj_key = "{}.{}".format(args[0], args[1])
            if obj_key in objects:
                print(objects[obj_key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234.
        """
        args = line.split()
        if not line:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            obj_key = "{}.{}".format(args[0], args[1])
            if obj_key in objects:
                del objects[obj_key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances based or not
        on the class name. Ex: $ all BaseModel or $ all.
        """
        args = line.split()
        objects = storage.all()
        if not line:
            print([str(obj) for obj in objects.values()])
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        else:
            print([str(obj) for obj in objects.values() if args[0] in str(obj)])

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        args = line.split()
        objects = storage.all()
        if not line:
            print("** class name missing **")
        elif args[0] not in ["BaseModel"]:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(args[0], args[1])
            if obj_key not in objects:
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                obj = objects[obj_key]
                setattr(obj, args[2], args[3])
                obj.save()

    def do_quit(self, line):
        """Quit command to exit the program"""
        sys.exit()

    def do_EOF(self, line):
        """EOF command to exit the program"""
        print()
        sys.exit()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
