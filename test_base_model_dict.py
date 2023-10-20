#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel, "State": State, "City": City, "Amenity": Amenity, "Place": Place, "Review": Review}

    def do_create(self, args):
        """Create a new instance of a specified class"""
        if not args:
            print("** class name missing **")
            return

        args = args.split()
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        new_instance = self.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, args):
        """Show the string representation of an instance"""
        if not args:
            print("** class name missing **")
            return

        args = args.split()
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        obj_key = "{}.{}".format(class_name, obj_id)
        objects = storage.all(self.classes[class_name])
        if obj_key in objects:
            print(objects[obj_key])
        else:
            print("** no instance found **")

    # Add similar methods for do_destroy, do_all, and do_update

    def emptyline(self):
        pass

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """Handle EOF (Ctrl+D) to exit the program"""
        print("")
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
