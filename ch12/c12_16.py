"""c12_16.py"""

list_i = [10, 20, 30, 40, 50]
L = len(list_i)
with open("test_3.bin", "wb") as f:
    list_b = [i.to_bytes(4, byteorder="little") for i in list_i]
    f.writelines(list_b)

with open("test_3.bin", "rb") as f:
    for i in range(L):
        b = f.read(4)
        i = int.from_bytes(b, byteorder="little")
        print(i, end=" ")
