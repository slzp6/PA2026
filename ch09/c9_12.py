"""c9_12.py"""


def my_decorator(original_function):
    """my decorator"""

    def wrapper(*args):
        print("=== args: ", args)
        result = original_function(*args)
        print("=== result: ", result)
        return result

    return wrapper


@my_decorator
def calc_product(x, y):
    """calculate the product of two numbers"""
    return x * y


R = calc_product(10, 20)
print(R)
