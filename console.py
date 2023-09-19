#!/usr/bin/python3
import cmd
import sys
from models.base_model import BaseModel
from models import storage
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.user import User
from models.state import State
from models.review import Review

def parse(arg):
    """Defines parse module"""

    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

<<<<<<< HEAD
    def do_create(self, line):
        """Create a new instance of BaseModel, saves it (to the JSON file),
        and prints the id. Ex: $ create BaseModel
        """
        if not line:
=======
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

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
>>>>>>> fd326bc9c570513109830c5aa602a225eda40dc8
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

<<<<<<< HEAD
    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".
        """
        args = line.split()
        objects = storage.all()
        if not line:
=======

    def help_all(self):
        """ help_all Help information for the all command """
        print("Shows all objects, or all of a class")
        print("[Usage]: all <className>\n")

    def help_count(self):
        """ print help information for the count"""
        print("Usage: count <class_name>")

    def help_update(self):
        """ Help information for the update class """
        print("Updates an object with new information")
        print("Usage: update <className> <id> <attName> <attVal>\n")


    def help_quit(self):
        """
        Prints the help documentation for the 'quit' command.
        """
        print("Exits the program with formatting\n")

    def help_EOF(self):
        """ help EOF Prints the help documentation for EOF """
        print("Exits the program without formatting\n")

    def help_create(self):
        """ help_create Help information for the create method """
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")


    def help_show(self):
        """ help_show Help information for the show command """
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")

    def help_destroy(self):
        """ help_destroy Help information for the destroy command """
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")


    def do_update(self, arg):
        """Update an instance attribute."""
        args = arg.split()
        if not args:
>>>>>>> fd326bc9c570513109830c5aa602a225eda40dc8
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

    def default(self, arg):
        """default module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
