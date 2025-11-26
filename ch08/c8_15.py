"""c8_15.py"""


def recur_a(i):
    """function a"""
    if i >= 3:
        return
    print(i, end=' ')
    recur_a(i + 1)


recur_a(0)
