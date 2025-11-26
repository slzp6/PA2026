"""c9_7.py"""

# pylint: disable=missing-function-docstring


def nlist_outer():
    numbers = []

    def nlist_inner(x):
        numbers.append(x)
        print(numbers)

    return nlist_inner


nlist = nlist_outer()

nlist(10)
nlist(20)
nlist(30)
