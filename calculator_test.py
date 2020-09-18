from calculator import Calculator
from pytest import approx, raises, fixture, mark


@fixture
def calculator():
    return Calculator()


def test_can_add_two_numbers(calculator):
    assert calculator.add(1, 2) == 3
    assert calculator.add(1, 4) == 5


def test_can_add_three_numbers(calculator):
    assert calculator.add(1, 2, 3) == 6


def test_can_add_many_numbers(calculator):
    assert calculator.add(*range(100)) == 4950


def test_can_subtract_two_numbers(calculator):
    assert calculator.sub(10, 3) == 7
    assert calculator.sub(19, 9) == 10


def test_can_multiply_two_numbers(calculator):
    assert calculator.mul(10, 3) == 30
    assert calculator.mul(10, 4) == 40


def test_can_multiply_three_numbers(calculator):
    assert calculator.mul(10, 3, 10) == 300


def test_can_multiply_many_numbers(calculator):
    assert calculator.mul(*range(1, 11)) == 3628800


def test_can_divide_two_numbers(calculator):
    assert calculator.div(10, 2) == 5.0


def test_dividing_by_zero_returns_inf(calculator):
    assert calculator.div(10, 0) == "inf"


def test_raises_an_exception_when_multiply_by_zero(calculator):
    with raises(ValueError):
        calculator.mul(10, 0)


def test_raises_an_exception_when_multiplying_with_a_falsy_value(calculator):
    with raises(ValueError):
        calculator.mul(10, None)


@mark.parametrize("test_input, expected", [([1, 2, 3], 2), ([4, 5, 6], 5), ([4, 5, 5], 4.67)])
def test_returns_the_average_of_three_numbers(test_input, expected, calculator):
    assert calculator.avg(test_input) == approx(expected, 0.1)


def test_returns_the_average_of_one_number(calculator):
    assert calculator.avg([1]) == 1
    assert calculator.avg([4]) == 4
