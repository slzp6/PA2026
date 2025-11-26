"""c9_2.py"""


def print_hello(name):
    """print hello"""
    print("Hello,", name)
    return name.upper()


S = print_hello("Tom")
print(S)
