"""c9_8.py"""


def my_decorator(original_function):
    """my decorator"""

    def wrapper():
        print("--- before the function call. ---")
        original_function()
        print("--- after the function call. ---")

    return wrapper


@my_decorator
def print_hello():
    """print Hello"""
    print("Hello!")


print_hello()
