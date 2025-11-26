"""c9_4.py"""


def square(x):
    """square"""
    return x * x


def cube(x):
    """cube"""
    return x * x * x


def elements(func, iterable):
    """elements"""
    return [func(i) for i in iterable]


nums = [3, 4, 5]
print("original numbers:", nums)
print("squared numbers:", elements(square, nums))
print("cubed numbers:", elements(cube, nums))
