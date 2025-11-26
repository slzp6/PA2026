"""c11_3.py"""

# pylint: disable=too-few-public-methods


class Person:
    """person class"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        """print name"""
        print(self.name)


p1 = Person("Taro", 30)
p1.print_name()

print(dir(p1))
