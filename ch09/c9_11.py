"""c9_11.py"""


def my_decorator(original_function):
    """my decorator"""

    def wrapper(*args):
        print("--- before the function call ---")
        print("=== args: ", args)
        original_function(*args)
        print("--- after the function call ---")

    return wrapper


@my_decorator
def print_hello(first_name, last_name):
    """print Hello, first name and last name"""
    print("Hello, ", first_name, last_name)


print_hello("John", "Doe")
