"""c7_13.py"""


def multiply_add(x, y=300, z=400):
    """multiply and add"""
    return x * y + z


print(multiply_add(10))
print(multiply_add(10, z=20))
print(multiply_add(10, z=200, y=300))

# TypeError: multiply_add()
# missing 1 required positional
# argument: 'x'
#  print(multiply_add(y=20, z=30))
