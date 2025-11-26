"""c11_7.py"""

# pylint: disable=too-few-public-methods
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring


class A:

    def print_msg(self):
        print("class A")


class B(A):

    def print_msg(self):
        print("class B")


class C(A):

    def print_msg(self):
        print("class C")


class D(B, C):
    pass


d = D()
d.print_msg()

print(D.__mro__)
print(D.mro())
