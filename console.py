#!/usr/bin/python3

""" Console Module """
import cmd  # Import the 'cmd' module to create an interactive console
import sys  # Import the 'sys' module to handle command-line arguments

# Define the RbnbConsole class, which inherits from cmd.Cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "  # Set the prompt (command prompt) for the console

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
# Function to run the console in interactive mode


def run_interactive():
    HBNBCommand().cmdloop()

# Function to run the console in non-interactive mode with an input file


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
