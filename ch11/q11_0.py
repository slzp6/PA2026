"""q11_0.py"""


def trapezoid_area(base_a, base_b, height):
    """calculate area of a trapezoid"""
    return (base_a + base_b) * height / 2.00


A = trapezoid_area(3.0, 4.0, 5.0)
print(A)
