"""c12_15.py"""

with open("test_2.bin", "rb") as f:
    b = f.read(4)
    i = int.from_bytes(b, byteorder="little")
    print(type(i))
    print(i)

memv = memoryview(b)
print(memv.cast('i').tolist())
