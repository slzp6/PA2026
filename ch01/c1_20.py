"""c1_20.py"""

DAT_1024 = b'A' * 1024
memv = memoryview(DAT_1024)
memv_sli = memv[0:32]
print(memv_sli)
print(type(memv_sli))
print(bytes(memv_sli))
