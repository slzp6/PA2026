"""q7_1.py"""

import math


def sphere_volume(r):
    """sphere volume"""
    return (4.0 / 3.0) * (math.pi) * r**3


SV = sphere_volume(3.0)
print(f"{SV:.2f}")
