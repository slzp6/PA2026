"""c12_1.py"""

# pylint: disable=consider-using-with

f = open("fruits.txt", "r", encoding="utf8")
txt = f.read()
f.close()

print(txt)
print(type(txt))
