#!/usr/bin/python3
import cmd
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "State", "City", "Amenity",
               "Place", "Review"]

    def emptyline(self):
        pass

    def do_EOF(self, line):
        return True

    def do_quit(self, line):
        return True

    def do_create(self, line):
        if line == "":
            print("** class name missing **")
        elif line in self.classes:
            b = eval(line)()
            b.save()
            print(b.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        token = line.split(" ")
        search = storage.all()
        if token[0] is "":
            print("** class name missing **")
        elif token[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(token) < 2:
            print("** instance id missing **")
        elif token[0] + "." + token[1] not in search:
            print("** no instance found **")
        else:
            obj = search[token[0] + "." + token[1]]
            print(obj)

    def do_destroy(self, line):
        token = line.split(" ")
        search = storage.all()
        if token[0] is "":
            print("** class name missing **")
        elif token[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(token) < 2:
            print("** instance id missing **")
        elif token[0] + "." + token[1] not in search:
            print("** no instance found **")
        else:
            del search[token[0] + "." + token[1]]
            storage.__objects = search
            storage.save()

    def do_update(self, line):
        token = line.split(" ")
        search = storage.all()
        if token[0] is "":
            print("** class name missing **")
        elif token[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(token) < 2:
            print("** instance id missing **")
        elif token[0] + "." + token[1] not in search:
            print("** no instance found **")
        elif len(token) < 3:
            print("** attribute name missing **")
        elif len(token) < 4:
            print("** value missing **")
        else:
            obj = search[token[0] + "." + token[1]]
            storage.__objects = obj.__dict__
            storage.__objects[token[2]] = token[3]
            storage.save()

    def do_all(self, line):
        dic = storage.all()
        lis = []
        if line is "":
            for k in dic.keys():
                lis.append(str(dic[k]))
            print(lis)
        elif line not in self.classes:
            print("** class doesn't exist **")
        else:
            for k in dic.keys():
                if line in k:
                    lis.append(str(dic[k]))
            print(lis)

    def help_quit(self):
        print("Exit the program")

    def help_EOF(self):
        print("Exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
