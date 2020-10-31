import abc
import re
import sys
from Banana_error import Type_Error

VarDict = {}
DefDict = {}


# def Banana_print(args: list):
#     for item in args:
#         sys.stdout.write(str(item)+'\n')
#
#
# def Banana_add(args: list):
#     out = args[0]
#     for item in args[1:]:
#         try:
#             out += item
#         except TypeError:
#             ra = Type_Error()
#             ra.Say = f"Type_Error: unsupported add: {type(out)} and {type(item)}"
#             ra.Raise_Error()
#     return out
#
#
# def Banana_multiplication(args: list):
#     out = args[0]
#     for item in args[1:]:
#         try:
#             out *= item
#         except TypeError:
#             ra = Type_Error()
#             ra.Say = f"Type_Error: unsupported multiplication: {type(out)} and {type(item)}"
#             ra.Raise_Error()
#     return out
#
#
# def Banana_division(args: list):
#     out = args[0]
#     for item in args[1:]:
#         try:
#             out /= item
#         except TypeError:
#             ra = Type_Error()
#             ra.Say = f"Type_Error: unsupported division: {type(out)} and {type(item)}"
#             ra.Raise_Error()
#     return out
#
#
# def Banana_power(args: list):
#     out = args[0]
#     for item in args[1:]:
#         try:
#             out **= item
#         except TypeError:
#             ra = Type_Error()
#             ra.Say = f"Type_Error: unsupported power: {type(out)} and {type(item)}"
#             ra.Raise_Error()
#     return out
#
#
# def Banana_set(args: list):
#     VarDict[args[0]] = args[1]
#     # print(var)
#
#
# def Banana_input(args: list):
#     return input(args[0])
#
#
# def Banana_int(args: list):
#     return int(args[0])
#
#
# def Banana_str(args: list):
#     return str(args[0])
#
#
# def Banana_run(args: list):
#     pass
#
#
# def Banana_if(args: list):
#     # args[1]()
#     if bool(args[0]):
#         args[1]()
#
#
# def Banana_equal(args: list):
#     return args[0] == args[1]
#
#
# DefList = {'print': Banana_print, 'add': Banana_add, 'multiplication': Banana_multiplication,
#            'division': Banana_division, 'int': Banana_int, 'str': Banana_str, 'input': Banana_input,
#            'power': Banana_power, 'set': Banana_set, 'run': Banana_run, 'if': Banana_if}


class Banana_def(metaclass=abc.ABCMeta):
    def __init__(self):
        self.DefSelf = 'CallSelf'
        self.Set = 'Set'
        self.Run = "Run"
        DefDict[self.__class__.__name__[7:]] = self

    @abc.abstractmethod
    def call(self, args):
        pass


class Banana_set(Banana_def):
    def __init__(self):
        super().__init__()
        self.args = {0: [self.Set], 1: []}

    def call(self, args):
        VarDict[args[0]] = args[1]


Banana_set()


class Banana_print(Banana_def):
    def __init__(self):
        super().__init__()
        self.args = {'all': []}

    def call(self, args):
        for item in args:
            sys.stdout.write(str(item) + '\n')


Banana_print()


class Banana_add(Banana_def):
    def __init__(self):
        super().__init__()
        self.args = {"all": []}

    def call(self, args):
        out = args[0]
        for item in args[1:]:
            try:
                out += item
            except TypeError:
                ra = Type_Error()
                ra.Say = f"Type_Error: unsupported add: {type(out)} and {type(item)}"
                ra.Raise_Error()
        return out


Banana_add()


class Banana_subtraction(Banana_def):
    def __init__(self):
        super().__init__()
        self.args = {0: [], 1: []}

    def call(self, args):
        out = args[0]
        for item in args[1:]:
            try:
                out -= item
            except TypeError:
                ra = Type_Error()
                ra.Say = f"Type_Error: unsupported subtraction: {type(out)} and {type(item)}"
                ra.Raise_Error()
        return out


Banana_subtraction()


class Banana_power(Banana_def):
    def __init__(self):
        super().__init__()
        self.args = {"all": []}

    def call(self, args):
        out = args[0]
        for item in args[1:]:
            try:
                out **= item
            except TypeError:
                ra = Type_Error()
                ra.Say = f"Type_Error: unsupported power: {type(out)} and {type(item)}"
                ra.Raise_Error()
        return out


Banana_power()


class Banana_multiplication(Banana_def):
    def __init__(self):
        super().__init__()
        self.args = {"all": []}

    def call(self, args):
        out = args[0]
        for item in args[1:]:
            try:
                out *= item
            except TypeError:
                ra = Type_Error()
                ra.Say = f"Type_Error: unsupported multiplication: {type(out)} and {type(item)}"
                ra.Raise_Error()
        return out


Banana_multiplication()


class Banana_division(Banana_def):
    def __init__(self):
        super().__init__()
        self.args = {"all": []}

    def call(self, args):
        out = args[0]
        for item in args[1:]:
            try:
                out /= item
            except TypeError:
                ra = Type_Error()
                ra.Say = f"Type_Error: unsupported division: {type(out)} and {type(item)}"
                ra.Raise_Error()
        return out


Banana_division()


class Banana_input(Banana_def):
    def __init__(self):
        super().__init__()
        self.args = {0: []}

    def call(self, args):
        out = input(args[0])
        if re.match(r'^[+-]?(0|([1-9]\d*))(\.\d+)?', out) is not None:
            if re.match(r'^[+-]?(0|([1-9]\d*))(\.\d+)?', out).span()[1] == len(out):
                if int(out) == float(out):
                    out = int(out)
                else:
                    out = float(out)
        return out


Banana_input()


class Banana_if(Banana_def):
    def __init__(self):
        super().__init__()
        self.args = {0: [], 1: [self.Run], 2: [self.Run]}

    def call(self, args):
        if args[0]:
            for item in args[1]:
                item()
        else:
            if len(args) > 2:
                for item in args[2]:
                    item()


Banana_if()


class Banana_equal(Banana_def):
    def __init__(self):
        super().__init__()
        self.args = {}

    def call(self, args):
        return args[0] == args[1]


Banana_equal()


class Banana_unequal(Banana_def):
    def __init__(self):
        super().__init__()
        self.args = {}

    def call(self, args):
        return args[0] != args[1]


Banana_unequal()
