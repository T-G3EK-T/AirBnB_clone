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
    
    def do_create(self, line):
        """
        Usage: katcreayi <class> <key1> = <value1> <key2> = <value2> ...
        """
        try:
            if not line:
                raise SyntaxError("No input provided")
    
            parts = line.split(" ")
            class_name = parts[0]
            args = parts[1:]
    
            kwargs = {}
            for arg in args:
                key, value = arg.split("=")
                value = value.strip().strip('"').replace("_", " ")
    
                kwargs[key] = value
    
            if not kwargs:
                obj = eval(class_name)()
            else:
                obj = eval(class_name)(**kwargs)
                # Assuming `storage` is defined somewhere
                storage.new(obj)
    
            print(obj.id)
            obj.save()
    
        except SyntaxError:
            print("** Class name or input format is missing or incorrect **")
        except NameError:
            print("** Class doesn't exist **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
