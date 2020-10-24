import sys

from Banana_Def import DefList, VarDict
from Banana_Error import Name_Error
import re


def run(line):
    LineList = SafeFind(line, [' '])
    # print(LineList[0], list(all.keys()))
    if LineList[0] in list(DefList.keys()):
        if LineList[0] == 'set':
            out = lambda: DefList[LineList[0]](arg(LineList[1:], IfSet=0))
            return out
        out = lambda: DefList[LineList[0]](arg(LineList[1:]))
        return out
    else:
        ra = Name_Error()
        ra.Say = f"name '{LineList[0]}' is not defined"
        ra.Raise_Error()


def arg(Arg: list, IfSet=None):
    out = []
    for time, item in enumerate(Arg):
        if (item[0] == '"' or item[0] == "'") and (item[len(item) - 1] == '"' or item[len(item) - 1] == "'"):
            out.append(item[1:len(item) - 1])
        elif re.match(r'^[+-]?(0|([1-9]\d*))(\.\d+)?', item) is not None:
            if re.match(r'^[+-]?(0|([1-9]\d*))(\.\d+)?', item).span()[1] == len(item):
                if item.find(".") == -1:
                    out.append(int(item))
                else:
                    out.append(float(item))
        elif item[0] == '(' and item[len(item) - 1] == ")":
            runs = item[1: len(item) - 1]
            out.append(run(runs)())
            # print(out)
        elif item in list(VarDict.keys()):
            out.append(VarDict[item])
        else:
            if IfSet is not None:
                if IfSet == time:
                    out.append(item)
    return out


def SafeFind(string: str, sep: list):
    InBrackets = False
    Brackets = ""
    Bracket = 0
    Out = []
    Last = 0
    for time, i in enumerate(string):
        if i in sep and not InBrackets and Bracket == 0:
            Out.append(string[Last + 1 if Last != 0 else 0:time])
            Last = time
        if i == '"' or i == "'":
            if Brackets == "":
                Brackets = i
                InBrackets = not InBrackets
            else:
                if Brackets == i:
                    InBrackets = not InBrackets
                    Brackets = ""
                else:
                    pass
        elif i == '(':
            Bracket += 1
        elif i == ')':
            Bracket -= 1
    Out.append(string[Last + 1 if Last != 0 else 0:])
    return Out


class Banana:
    def __init__(self, code):
        self.CodeList = SafeFind(code, ['\n'])
        self.RunList = []
        self.TimeDict = {}

    def compile(self):
        for item in self.CodeList:
            self.RunList.append(run(item))

    def run(self):
        self.compile()
        for item in self.RunList:
            item()
