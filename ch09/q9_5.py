"""q9_5.py"""


def decorator_a(original_function):
    """decorator a"""

    def wrapper(*args):
        print("- A0 -")
        x = original_function(*args)
        print("- A1 -")
        return x * 2.0

    return wrapper


def decorator_b(original_function):
    """decorator b"""

    def wrapper(*args):
        print("- B0 -")
        x = original_function(*args)
        print("- B1 -")
        return x + 3.0

    return wrapper


@decorator_a
@decorator_b
def numbers():
    """return 10.0"""
    return 10.0


print(numbers())
