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
        if ut is not None:
            iterable = (x for x in iterable if x <= ut)
        if lt is not None:
            iterable = (x for x in iterable if x >= lt)
        try:
            return mean(iterable)
        except StatisticsError:
            return 0
