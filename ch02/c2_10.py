"""c2_10.py"""

for i in range(8, 16):
    print(f"{i:02} {bin(i):>6}", end="")
    print(f"{oct(i):>5}", end="")
    print(f"{hex(i):>4}")
