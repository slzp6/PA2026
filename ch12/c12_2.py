"""c12_2.py"""

# pylint: disable=consider-using-with

f = open("fruits.txt", "r", encoding="utf8")
txt_1 = f.readline()
print(txt_1)
txt_2 = f.readline()
print(txt_2)
txt_3 = f.readline()
print(txt_3)
f.close()
