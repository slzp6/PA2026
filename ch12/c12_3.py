"""c12_3.py"""

# pylint: disable=consider-using-with

f = open("fruits.txt", "r", encoding="utf8")
for line in f:
    print(line)
f.close()
