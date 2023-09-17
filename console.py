#!/usr/bin/python3

""" Console Module """
import cmd 
import sys  

# Define the RbnbConsole class, which inherits from cmd.Cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    
    # Set the prompt (command prompt) for the console

    # Method for the 'help' command
    def do_help(self, arg):
        """Show help message."""
        print("Documented commands (type help <topic>):")
        print("========================================")
        print("EOF  help  quit")

    # Method for the 'EOF' (End of File) command
    def do_EOF(self, arg):
        """Exit the console gracefully when
        the EOF command (Ctrl+D) is entered."""
        print("\nExiting the console.")
        return True

    # Method for the 'quit' command
    def do_quit(self, arg):
        """quit the console."""
        return True

    def handle_empty_line(self):
        """an empty line."""
        pass

    def do_create(self, args):
        """ Create an object of any class.Usage: create <className> """
        if not args:
            print("** class name missing **")
            return
        elif args not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.classes[args]()
        storage.save()
        print(new_instance.id)
        storage.save()

    def help_create(self):
        """
        Help information for the create method.
        """
        print("Creates an instance of a class")
        print("[Usage]: create <className>\n")

    def do_show(self, args):
        """
        Show an individual object.
        
        Usage: show <className> <objectId>
        """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]

        # Guard against trailing args
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id
        try:
            print(storage._FileStorage__objects[key])
        except KeyError:
            print("** no instance found **")

    def help_show(self):
        """
        Help information for the show command.
        """
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")

    def do_destroy(self, args):
        """
        Destroys a specified object.
        
        Usage: destroy <className> <objectId>
        """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id

        try:
            del(storage.all()[key])
            storage.save()
        except KeyError:
            print("** no instance found **")

    def help_destroy(self):
        """
        Help information for the destroy command.
        """
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")
    
# THE Function run the console in interactive mode


def run_interactive():
    HBNBCommand().cmdloop()

# This Function run the console in non-interactive mode with an input file


def run_non_interactive(input_file):
    console = HBNBCommand()
    console.use_rawinput = False  # Disable raw input (non-interactive mode)
    with open(input_file, "r") as f:
        lines = f.readlines()  # Read all lines from the input file
        print("\n")  # Print an empty line before the message
        for line in lines:
            console.onecmd(line.strip())  # Process each line as a command

# Entry point of the program


if __name__ == '__main__':
    if len(sys.argv) == 1:
        # If no arguments are provided, run the console in intera
        run_interactive()
    elif len(sys.argv) == 2:
        # If one argument (input file name) is provided,
        # run in non-interactive mode
        run_non_interactive(sys.argv[1])
    else:
        # If more than one argument is provided, display a usage message
        print("Usage: python console.py [input_file]")
