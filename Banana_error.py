import abc
import sys


class Banana_Error(metaclass=abc.ABCMeta):
    Name = None
    Say = None

    def Raise_Error(self):
        print(f'{self.Name}: {self.Say}', file=sys.stderr)
        sys.exit(1)


class Arg_Error(Banana_Error):
    Name = 'Arg_Error'


class Name_Error(Banana_Error):
    Name = 'Name_Error'


class Type_Error(Banana_Error):
    Name = 'Type_Error'


def Banana_raise(error, say):
    out = error()
    out.Say = say
    out.Raise_Error()
