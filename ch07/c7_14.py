"""c7_14.py"""


def vl_add(*x):
    """add"""
    print(type(x))
    print(x)
    s = 0
    for i in x:
        s += i
    return s


print(vl_add(10, 20, 30, 40))
