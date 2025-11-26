"""c7_12.py"""


def multiply_add(x, y=300, z=400):
    """multiply and add"""
    return x * y + z


print(multiply_add(10, y=20, z=30))
print(multiply_add(10, z=30, y=20))
