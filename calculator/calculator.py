from math import prod
from statistics import mean, StatisticsError


def add(*args):
    return sum(args)


def sub(minuend, subtrahend):
    return minuend - subtrahend


def mul(*args):
    if not all(args):
        raise ValueError
    return prod(args)


def div(numerator, denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return "inf"


def avg(iterable, ut=None, lt=None):
    if ut is not None:
        iterable = (x for x in iterable if x <= ut)
    if lt is not None:
        iterable = (x for x in iterable if x >= lt)
    try:
        return mean(iterable)
    except StatisticsError:
        return 0
