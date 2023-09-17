#!/usr/bin/python3

"""Modules of  the HBnB console."""
import cmd
import sys

def do_quit(self, arg):
    """
    This command allows you to gracefully exit the program.
    """
    return True

def do_EOF(self, arg):
    """
    This command allows you to exit the program using the EOF (End of File) signal, typically Ctrl+D.
    """
    print("")
    return True

def do_create(self, arg):
    """
    This command creates a new instance of a specified class and prints its unique id.
    """
    argl = parse(arg)
    if len(argl) == 0:
        print("** class name missing **")
    elif argl[0] not in HBNBCommand.__classes:
        print("** class doesn't exist **")
    else:
        print(eval(argl[0])().id)
        storage.save()

def do_show(self, arg):
    """
    This command displays the string representation of a class instance based on its class and id.
    """
    argl = parse(arg)
    objdict = storage.all()
    if len(argl) == 0:
        print("** class name missing **")
    elif argl[0] not in HBNBCommand.__classes:
        print("** class doesn't exist **")
    elif len(argl) == 1:
        print("** instance id missing **")
    elif "{}.{}".format(argl[0], argl[1]) not in objdict:
        print("** no instance found **")
    else:
        print(objdict["{}.{}".format(argl[0], argl[1])])

def do_destroy(self, arg):
    """
    This command deletes a class instance based on its class and id.
    """
    argl = parse(arg)
    objdict = storage.all()
    if len(argl) == 0:
        print("** class name missing **")
    elif argl[0] not in HBNBCommand.__classes:
        print("** class doesn't exist **")
    elif len(argl) == 1:
        print("** instance id missing **")
    elif "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
        print("** no instance found **")
    else:
        del objdict["{}.{}".format(argl[0], argl[1])]
        storage.save()

def do_all(self, arg):
    """
    This command displays the string representations of instances of a specified class or all instances.    
    """
    argl = parse(arg)
    if len(argl) > 0 and argl[0] not in HBNBCommand.__classes:
        print("** class doesn't exist **")
    else:
        objl = []
        for obj in storage.all().values():
            if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                objl.append(obj.__str__())
            elif len(argl) == 0:
                objl.append(obj.__str__())
        print(objl)

def do_count(self, arg):
    """
    This command retrieves and prints the number of instances of a specified class.
    """
    argl = parse(arg)
    count = 0
    for obj in storage.all().values():
        if argl[0] == obj.__class__.__name__:
            count += 1
    print(count)

