"""c9_3.py"""


def trace(func):
    """trace function"""

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__} {args} -> {result}")
        return result

    return wrapper


@trace
def fibonacci(n):
    """fibonacci function"""
    if n == 1:
        return 0
    if n == 2:
        return 1
    return (fibonacci(n - 2) + fibonacci(n - 1))


fibonacci(6)
