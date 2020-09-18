from functools import reduce
from math import prod


class Calculator:

    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def sub(minuend, subtrahend):
        return minuend - subtrahend

    @staticmethod
    def mul(*args):
        return prod(args)
