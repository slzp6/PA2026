"""c11_6.py"""

# pylint: disable=too-few-public-methods
# pylint: disable=missing-class-docstring


class X:
    pass


class Y:
    pass


class Z:
    pass


class M(X, Y, Z):
    pass


print(M.__mro__)
print(M.mro())
