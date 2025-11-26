"""c1_19.py"""

B = b"Tokyo"
print(B, type(B))
# B[0] = 65
# 'bytes' object does not support item assignment

BA = bytearray(b"Tokyo")
print(BA, type(BA))

BA[0] = 65
print(BA)
