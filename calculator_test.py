from calculator import Calculator


def test_can_add_two_numbers():
    calculator = Calculator()
    assert calculator.add(1, 2) == 3
    assert calculator.add(1, 4) == 5


def test_can_add_three_numbers():
    calculator = Calculator()
    assert calculator.add(1, 2, 3) == 6


def test_can_add_many_numbers():
    calculator = Calculator()
    assert calculator.add(*range(100)) == 4950


def test_can_subtract_two_numbers():
    calculator = Calculator()
    assert calculator.sub(10, 3) == 7
