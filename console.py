#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    def do_EOF(self, line):
        return True
    def do_quit(self, line):
        return True
    def help_quit(self):
        print("Exit the program")
    def help_EOF(self):
        print("Exit the program")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
