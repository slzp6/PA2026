"""q11_1.py"""

# pylint: disable=too-few-public-methods


class Trapezoid:
    """class trapezoid"""

    def __init__(self, base_a, base_b, height):
        self.base_a = base_a
        self.base_b = base_b
        self.height = height

    def area(self):
        """calculate area of a trapezoid"""
        return (self.base_a + self.base_b) * self.height / 2.00


area_t = Trapezoid(3.0, 4.0, 5.0)
print(area_t.area())
