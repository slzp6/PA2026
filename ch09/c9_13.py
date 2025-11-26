"""c9_13.py"""


def my_decorator(original_function):
    """my decorator"""

    def wrapper(*args, **kwargs):
        print("=== args: ", args)
        print("=== kwargs: ", kwargs)
        result = original_function(*args, **kwargs)
        print("=== result: ", result)
        return result

    return wrapper


@my_decorator
def calc_product(x, y):
    """calculate the product of two numbers"""
    return x * y


P1 = calc_product(10, 20)
print(P1)

print("")
P2 = calc_product(x=30, y=40)
print(P2)

print("")
P3 = calc_product(50, y=60)
print(P3)
