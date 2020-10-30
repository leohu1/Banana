import re

from Banana_def import DefDict, VarDict
from Banana_error import Name_Error, Arg_Error, Banana_raise


def run(line):
    LineList = SafeFind(line, [' '])
    # print(LineList[0], list(all.keys()))
    if LineList[0] in list(DefDict.keys()):
        out = lambda: DefDict[LineList[0]].call(arg(LineList[1:], DefDict[LineList[0]].args))
        return out
    else:
        ra = Name_Error()
        ra.Say = f"name '{LineList[0]}' is not defined"
        ra.Raise_Error()


def arg(Arg: list, args: dict):
    out = []
    for time, item in enumerate(Arg):
        TimeArgs = args.get(time) if args.get(time) is not None else (
            args.get('all') if args.get('all') is not None else [])
        if "Run" in TimeArgs and item[0] == '{' and item[len(item) - 1] == '}':
            outIn = []
            for i in SafeFind(item[1:len(item) - 1], [';']):
                outIn.append(run(i))
            out.append(outIn)
        elif (item[0] == '"' or item[0] == "'") and (item[len(item) - 1] == '"' or item[len(item) - 1] == "'"):
            out.append(item[1:len(item) - 1])
        elif re.match(r'^[+-]?(0|([1-9]\d*))(\.\d+)?', item) is not None:
            if re.match(r'^[+-]?(0|([1-9]\d*))(\.\d+)?', item).span()[1] == len(item):
                if item.find(".") == -1:
                    out.append(int(item))
                else:
                    out.append(float(item))
        elif item[0] == '(' and item[len(item) - 1] == ")":
            runs = item[1: len(item) - 1]
            if 'CallSelf' in TimeArgs:
                out.append(run(runs))
            else:
                out.append(run(runs)())
            # print(out)
        elif item in list(VarDict.keys()):
            out.append(VarDict[item])
        elif 'Set' in TimeArgs:
            out.append(item)
        else:
            Banana_raise(Arg_Error, f"No arg type(at '{item}).")
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
        elif i == '(' or i == '{':
            Bracket += 1
        elif i == ')' or i == '}':
            Bracket -= 1
    Out.append(string[Last + 1 if Last != 0 else 0:])
    return Out


class Banana:
    def __init__(self, code):
        self.CodeList = SafeFind(code, ['\n'])
        self.CompileList = []
        self.TimeDict = {}

    def compile(self):
        for item in self.CodeList:
            if item[0] == '#':
                continue
            self.CompileList.append(run(item))

    def run(self):
        self.compile()
        for item in self.CompileList:
            item()
