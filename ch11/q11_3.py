"""q11_3.py"""

# pylint: disable=too-few-public-methods


class MyClass:
    """my class"""
    x = 100


i = MyClass()
S = isinstance(i, MyClass)
print(S)
