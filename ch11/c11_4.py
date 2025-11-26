"""c11_4.py"""

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

p2 = Person("Jiro", 50)
p2.print_name()

p1.name = "Shiro"
p1.print_name()

del p2
if "p2" not in locals():
    print("--- p2 is not defined ---")
