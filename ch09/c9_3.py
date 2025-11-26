"""c9_3.py"""


def hello_upper(txt):
    """upper"""
    return txt.upper()


def hello_lower(txt):
    """lower"""
    return txt.lower()


def greet(func):
    """print hello"""
    print(func("Hello"))


greet(hello_upper)
greet(hello_lower)
