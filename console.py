#!/usr/bin/python3
"""project console"""
from models.user import User
from models.product import Product
from models.review import Review
from models.category import Category
from models.subcategory import Subcategory
from models.order import Order
from models.delivery import Delivery
from models.brand import Brand
import models
import cmd

classes = {"user": User, "product": Product, "review": Review, "category": Category, "subcategory":Subcategory, "order": Order, "delivery": Delivery, "brand": Brand}


class FufilConsole(cmd.Cmd):
    """command line interaction with project"""

    def do_quit(self):
        """close console."""

        return True
    
    def do_help(self):
        """print information about console commands."""
        return True

    def emptyline(self):
        """dont accrpt empty line"""

        return False

    def do_create(self, line):
        """Create a new instance of a class"""

        args = line.split()
        if len(args) < 1:
            print("****Failed to provide a class name.****")
        else:
            if args[0] in classes:
                kwargs = self.create_kwargs(line)
                inst = classes[args[0]](**kwargs)
                inst.save()
                print(inst.id)
            else:
                print("****An invalid class was provides.""")

    def do_show(self, line):
        """Print a string representation of a particular class instance."""

        args = line.split()
        if len(args) > 0:
            if args[0] in classes:
                if len(args) > 1:
                    inst = models.storage.get(args[0], args[1])
                    if inst is not None:
                        print(inst)
                    else:
                        print("****NO such instance was FOUND.****")
                else:
                    print("****An invalid class id was provided.****")
            else:
                print("****An invalid class was provided****")
        else:
            print("****Failed to provide a class name****")

    def do_all(self, line):
        """Print a list of all instances of a class."""

        args = line.split()
        if len(args) > 0:
            if args[0] in classes:
                all_insts = models.storage.all(args[0])
                print(all_insts)
            else:
                print("****An invalid class was provided.****")
        else:
            print("****Failed to provide a class name****")
    def do_destroy(self, line):
        """Deletes an instanse  based on class and id."""

        args = line.split()
        if len(args) > 0:
            if args[0] in classes:
                if len(args) > 1:
                    inst = models.storage.get(args[0], args[1])
                    if inst is not None:
                        inst.delete()
                    else:
                        print("****No such instance was Found.****")
                else:
                    print("****An invalid id was provided****")
            else:
                print("****An invalid class was provided.****")
        else:
            print("****Failed to provide a class name****")

    def do_update(self, line):
        """Update an instanse based on class and id"""

        args = line.split()
        if len(args) > 0:
            if args[0] in classes:
                if len(args) > 1:
                    inst = models.storage.get(args[0], args[1])
                    if inst is not None:
                        if len(args) > 2:
                            if args[2] in inst.to_dict():
                                if len(args) > 3:
                                    new_inst = inst
                                    name = (inst.__class__.__name__).lower()
                                    new_inst = classes[name](**inst.__dict__)
                                    new_inst.__dict__[args[2]] = args[3]
                                    inst.delete()
                                    new_inst.save()
                                else:
                                    print("****attribute value is absent***")
                            else:
                                print("****No such attribute in instance.****")
                        else:
                            print("****No attribute was provided****")
                    else:
                        print("****No such instance was Found.****")
                else:
                    print("****An invalid id was provided.****")
            else:
                print("****An invalid class name was provided.****")
        else:
            print("****Failed to provide a class  name****")

    def create_kwargs(self, line):
        """Create a dictionary of key-word arguments from command line string"""

        idx = 0
        for j in range(len(line)):
            if line[j] == "{":
                idx = j
                break
        if id == 0:
            return None
        line = line[idx+1:-1]
        #splt the line by white space
        args = line.split(", ")
        kwargs = {}
        for i in range(len(args)):
            #split each value in args if separated by "=" or ":"
            if ':' not in args[i]:
                continue
            args[i] = args[i].replace("'", "")
            key_val = args[i].split(": ")
            #check if value is not an integer
            if key_val[1].isdigit():
                kwargs[key_val[0]] = int(key_val[1])
            #check if value is a float (a pair of ints separated by .)
            elif '.' in key_val[1]:
                dot_split = key_val[1].split('.')
                #check both pairs if the are valid integers"
                if dot_split[0].isdigit() and dot_split[1].isdigit():
                    kwargs[key_val[0]] = float(key_val[1])
                else:
                    kwargs[key_val[0]] = key_val[1]
            else:
                kwargs[key_val[0]] = key_val[1]
        return kwargs


if __name__ == "__main__":
    FufilConsole().cmdloop()
