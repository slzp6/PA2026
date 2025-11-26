"""c8_16.py"""


def recur_b(i):
    """function b"""
    if i >= 3:
        return
    recur_b(i + 1)
    print(i, end=' ')


recur_b(0)
