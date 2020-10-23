#!/Users/huqiwei/anaconda3/bin/python3
from Banana_core import Banana
from fire import Fire

# Banana(
# """set a 1
# print (add 10 a)"""
# ).run()


def main(file):
    """
    Banana language
    :param file: file name
    :return:
    """
    Data = open(file).read()
    Banana(Data).run()


if __name__ == '__main__':
    Fire(main)
