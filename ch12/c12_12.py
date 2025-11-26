"""c12_12.py"""

with open("test_1.bin", "rb") as f:
    str_bin = f.read()
    str_txt = str_bin.decode()
    print(type(str_txt))
    print(str_txt)
