"""c12_13.py"""

import sys

print(sys.byteorder)

N = 12190
print(f"N:   {N}")
print(f"bin: {bin(N)}")
print(f"hex: {hex(N)}")

print("---")
c = N.to_bytes(2, 'big').hex()
print(f"2 bytes; big:    {c}")
d = N.to_bytes(2, 'little').hex()
print(f"2 bytes; little: {d}")
