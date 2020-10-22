from .calculator import add, sub, avg, mul, div
from pytest import approx, raises, fixture, mark


def test_can_add_two_numbers():
    assert add(1, 2) == 3
    assert add(1, 4) == 5


def test_can_add_three_numbers():
    assert add(1, 2, 3) == 6


def test_can_add_many_numbers():
    assert add(*range(100)) == 4950


def test_can_subtract_two_numbers():
    assert sub(10, 3) == 7
    assert sub(19, 9) == 10


def test_can_multiply_two_numbers():
    assert mul(10, 3) == 30
    assert mul(10, 4) == 40


def test_can_multiply_three_numbers():
    assert mul(10, 3, 10) == 300


def test_can_multiply_many_numbers():
    assert mul(*range(1, 11)) == 3628800


def test_can_divide_two_numbers():
    assert div(10, 2) == 5.0


def test_dividing_by_zero_returns_inf():
    assert div(10, 0) == "inf"


def test_raises_an_exception_when_multiply_by_zero():
    with raises(ValueError):
        mul(10, 0)


def test_raises_an_exception_when_multiplying_with_a_falsy_value():
    with raises(ValueError):
        mul(10, None)


@mark.parametrize("test_input, expected", [([1, 2, 3], 2), ([4, 5, 6], 5), ([4, 5, 5], 4.67)])
def test_returns_the_average_of_three_numbers(test_input, expected, ):
    assert avg(test_input) == approx(expected, 0.1)


def test_returns_the_average_of_one_number():
    assert avg([1]) == 1
    assert avg([4]) == 4


@mark.parametrize("iterable_of_numbers, ut, expected", [([1, 2, 3, 51], 50, 2),
                                                        ([4, 5, 6], 49, 5),
                                                        ([4, 5, 5], 12, 4.67),
                                                        ([51, 1, 2, 4], 51, 14)])
def test_returns_the_average_of_a_list_with_the_upper_limit_removed(iterable_of_numbers, ut, expected):
    assert avg(iterable_of_numbers, ut=ut) == approx(expected, 0.1)


@mark.parametrize("iterable_of_numbers, lt, expected", [([1, 2, 3, 51], 50, 51),
                                                        ([4, 5, 6], 5, 6),
                                                        ([4, 4, 4], 4, 4),
                                                        ([51, 1, 2, 7], 2, 20)])
def test_returns_the_average_of_a_list_with_the_lower_limit_removed(iterable_of_numbers, lt, expected):
    assert avg(iterable_of_numbers, lt=lt) == approx(expected, 0.1)


def test_returns_zero_if_the_iterable_is_empty():
    assert avg([]) == 0


@mark.parametrize("iterable_of_numbers, lt, ut, expected", [([4, 5, 6], 2, 3, 0),
                                                            ([99, 108, 42], 0, 10, 0)])
def test_returns_zero_if_the_lower_threshold_and_upper_thresholds_make_the_iterator_empty(iterable_of_numbers, lt, ut, expected):
    assert avg(iterable_of_numbers, lt=lt, ut=ut) == 0


def test_returns_zero_if_lower_and_upper_thresholds_exist_but_empty_list():
    assert avg([], ut=25, lt=10) == 0


def test_can_deal_with_zero_as_lower_threshold_bound():
    assert avg([-1, 0, 1], lt=0) == 0.5


def test_can_deal_with_zero_as_upper_threshold_bound():
    assert avg([-1, 0, 1], ut=0) == -0.5
