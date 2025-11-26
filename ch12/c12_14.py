"""c12_14.py"""

with open("test_2.bin", "wb") as f:
    i = 100_000
    b = i.to_bytes(4, byteorder="little")
    print(type(b))
    f.write(b)
