"""c8_1.py"""


def func_a(x):
    """squared"""
    return x**2.0


# pylint: disable=unnecessary-lambda-assignment
func_b = lambda x: x**2.0

print(func_a(3.0))
print(func_b(3.0))
