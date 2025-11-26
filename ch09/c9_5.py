"""c9_5.py"""


def create_multiplier(factor):
    """create multiplier"""

    def multiplier(x):
        return x * factor

    return multiplier


double = create_multiplier(2)
triple = create_multiplier(3)

print(double(10))
print(triple(10))
