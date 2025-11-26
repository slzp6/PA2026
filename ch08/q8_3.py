"""q8_3.py"""


def recur(i):
    """function"""
    if i < 0:
        return
    recur(i - 1)
    print(i, end=' ')


recur(5)
