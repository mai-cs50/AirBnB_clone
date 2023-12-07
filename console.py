#!/usr/bin/python3
''' '''
import cmd
import re
from shlex import split
from models import storage
from model.base_models import BaseModel
from models.user import User
from models.state import State
from models.city import City

def parse(arg):
    curly_braces = re.search(r'\{(.*?)\}', arg)
    brackets = re.search(r'\[(.*?)\]', arg)
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
    ''' '''
    prompt = "(hbnb) "
    __classes = {
            "BaseModel",
            "User",
            "State",
            "City"
            }

    def emptyline(self):
        ''' '''
        pass

    def default(self, arg):
        ''' '''
        argdict = {
                "all": self.do_all,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "count": self.do_count,
                "update": self.do_update
                }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [argl[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("***Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        ''' '''
        return True

    def do_EOF(self):
        ''' '''
        print("")
        return True

    def do_creat(self):
        ''' '''
        try:
            if not line:
                raise SyntaxError()
            my_list = line.split(" ")

            kwargs = {}
            for i in range(1, len(my_list)):
                key, value = tuple(my_list[i].split("="))
                if value[0] = '"':
                    value = value.strip('"').replace("_", " ")
                else:
                    try:
                        value = eval(value)
                    except (SyntaxError, NameError):
                        continue
                kwargs[key] = value

            if kwargs == {}:
                obj = eval(my_list[0])()
            else:
                obj = eval(my_list[0])(**kwargs)
                storage.new(obj)
            print(obj.id)
            obj.save()

        except SyntaxError:
            print("** class name missing **")

        except NameError:
            print("** class doesn't exist **")

        def do_show(self, arg):
            ''' '''
            argl = parse(arg)
            objdict = storage.all()
            if len(argl) == 0:
                print("** class name missing **")
            elif argl[0] not in HBNBcommand.classes:
                print("** class doesn't exist **")
            elif len(argl) == 1:
                print("** instance id missing **")
            elif "{}.{}".format(argl[0], argl[1]) not in object:
                print("** no instance found **")
            else:
                print(objdict["{}.{}".format(argl[0], argl[1])])

        def do_destroy(self, arg):
            ''' '''
            argl = parse(arg)
            objdict = storage.all()
            if len(argl) == 0:
                print("** class name missing **")
            elif argl[0] not in HBNBcommand.classes:
                print("** class doesn't exist **")
            elif len(argl) == 1:
                print("** instance id missing **")
            elif "{}.{}".format(argl[0], argl[1]) not in object.keys():
                print("** no instance found **")
            else:
                del objdict["{}.{}".format(argl[0], argl[1])]
                storage.save()

        def do_all(self, arg):
            ''' '''
            argl = parse(arg)
            if len(argl) > 0 and argl[0] not in HBNBcommand.__classes:
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
