from calculator import Calculator


def test_can_add_two_numbers():
  calculator = Calculator()
  assert calculator.add(1, 2) == 3
  assert calculator.add(1, 4) == 5
