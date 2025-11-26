"""q8_1.py"""

import math


def sphere(radius):
    """Calculate surface area and volume."""
    area = 4.0 * math.pi * radius**2
    volume = (4.0 / 3.0) * (math.pi) * radius**3
    return area, volume


R = 5.0
s_area, s_volume = sphere(R)
print(f"radius: {R:.2f}")
print(f"area:   {s_area:.2f}")
print(f"volume: {s_volume:.2f}")
