import sys
from Banana_Error import Type_Error

VarDict = {}


def Banana_print(args: list):
    for item in args:
        sys.stdout.write(str(item))


def Banana_add(args: list):
    out = args[0]
    for item in args[1:]:
        try:
            out += item
        except TypeError:
            ra = Type_Error()
            ra.Say = f"Type_Error: unsupported add: {type(out)} and {type(item)}"
            ra.Raise_Error()
    return out


def Banana_multiplication(args: list):
    out = args[0]
    for item in args[1:]:
        try:
            out *= item
        except TypeError:
            ra = Type_Error()
            ra.Say = f"Type_Error: unsupported multiplication: {type(out)} and {type(item)}"
            ra.Raise_Error()
    return out


def Banana_division(args: list):
    out = args[0]
    for item in args[1:]:
        try:
            out /= item
        except TypeError:
            ra = Type_Error()
            ra.Say = f"Type_Error: unsupported division: {type(out)} and {type(item)}"
            ra.Raise_Error()
    return out


def Banana_power(args: list):
    out = args[0]
    for item in args[1:]:
        try:
            out **= item
        except TypeError:
            ra = Type_Error()
            ra.Say = f"Type_Error: unsupported power: {type(out)} and {type(item)}"
            ra.Raise_Error()
    return out


def Banana_set(args: list):
    VarDict[args[0]] = args[1]
    # print(var)


def Banana_input(args: list):
    return input(args[0])


def Banana_int(args: list):
    return int(args[0])


def Banana_str(args: list):
    return str(args[0])


DefList = {'print': Banana_print, 'add': Banana_add, 'multiplication': Banana_multiplication,
           'division': Banana_division, 'int': Banana_int, 'str': Banana_str, 'input': Banana_input,
           'power': Banana_power, 'set': Banana_set}
