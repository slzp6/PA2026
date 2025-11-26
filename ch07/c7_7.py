"""c7_7.py"""


def is_even(x):
    """is even"""
    print(x, end=": ")

    if x % 2 == 0:
        return True
    return False


print(is_even(2026))

# NameError: name 'x' is not defined
# print(x)
