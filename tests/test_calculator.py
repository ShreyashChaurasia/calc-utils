import pytest
from calc_utils.calculator import add, subtract, multiply, divide, power, factorial


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5


def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6
    assert multiply(0, 100) == 0


def test_divide():
    assert divide(10, 2) == 5
    assert divide(7, 2) == 3.5
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)


def test_power():
    assert power(2, 3) == 8
    assert power(9, 0.5) == 3


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120
    with pytest.raises(ValueError):
        factorial(-1)
    with pytest.raises(TypeError):
        factorial(3.5)
