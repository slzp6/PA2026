"""c9_9.py"""


def my_decorator(original_function):
    """my decorator"""

    def wrapper():
        print("--- before the function call. ---")
        original_function()
        print("--- after the function call. ---")

    return wrapper


def print_hello():
    """print Hello"""
    print("Hello!")


print_hello = my_decorator(print_hello)
print_hello()
