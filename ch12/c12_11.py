"""c12_11.py"""

with open("test_1.bin", "wb") as f:
    STR_TXT = "Hello, World!"
    STR_BIN = STR_TXT.encode()
    print(type(STR_BIN))
    f.write(STR_BIN)
