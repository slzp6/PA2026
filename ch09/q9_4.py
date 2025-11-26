"""q9_4.py"""

# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=invalid-name
# pylint: disable=too-few-public-methods


class nlist_outer():
    numbers = []

    def nlist_inner(self, x):
        self.numbers.append(x)
        print(self.numbers)


nlist = nlist_outer()

nlist.nlist_inner(10)
nlist.nlist_inner(20)
nlist.nlist_inner(30)
