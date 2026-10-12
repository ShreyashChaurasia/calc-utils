def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference between a and b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient of a divided by b. Raises ZeroDivisionError if b is zero."""
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


def power(base: float, exponent: float) -> float:
    """Return base raised to the power of exponent."""
    return base ** exponent


def factorial(n: int) -> int:
    """Return the factorial of a non-negative integer n."""
    if not isinstance(n, int):
        raise TypeError("factorial requires an integer")
    if n < 0:
        raise ValueError("factorial is not defined for negative numbers")
    if n in (0, 1):
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
