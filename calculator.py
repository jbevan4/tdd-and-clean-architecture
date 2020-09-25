from functools import reduce
from math import prod
from statistics import mean, StatisticsError


class Calculator:

    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def sub(minuend, subtrahend):
        return minuend - subtrahend

    @staticmethod
    def mul(*args):
        if not all(args):
            raise ValueError
        return prod(args)

    @staticmethod
    def div(numerator, denominator):
        try:
            return numerator / denominator
        except ZeroDivisionError:
            return "inf"

    @staticmethod
    def avg(iterable, ut=None, lt=None):
        if ut:
            iterable = filter(lambda x: x <= ut, iterable)
        if lt:
            iterable = filter(lambda x: x >= lt, iterable)
        try:
            return mean(iterable)
        except StatisticsError:
            return 0
