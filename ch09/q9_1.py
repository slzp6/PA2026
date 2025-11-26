"""q9_1.py"""


def create_adder(x):
    """create adder"""

    def adder(y):
        return x + y

    return adder


add_two = create_adder(2)
add_three = create_adder(3)

print(add_two(10))
print(add_three(10))

print(add_two(200))
print(add_three(200))
