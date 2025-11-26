"""c9_10.py"""


def my_decorator(original_function):
    """my decorator"""

    def wrapper(*args):
        print("--- before the function call ---")
        print("=== args: ", args)
        original_function(*args)
        print("--- after the function call ---")

    return wrapper


@my_decorator
def print_hello(name):
    """print Hello, name"""
    print("Hello, ", name)


print_hello("Tom")
