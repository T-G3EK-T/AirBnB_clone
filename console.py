#!/usr/bin/env python3
"""basic console program - airbnb clone"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, args):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """
        Exit the program on EOF (Ctrl+D)
        """
        print()  # Print a newline before exiting
        return True

    def emptyline(self):
        """
        Do nothing on an empty line
        """
        pass
    
    def do_create(self, arg):
        """
        Usage: create <Class name> <param 1> <param 2> <param 3>...
        arg: <key name>=<value> 
        """

if __name__ == "__main__":
    HBNBCommand().cmdloop()
