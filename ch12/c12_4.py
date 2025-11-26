"""c12_4.py"""

# pylint: disable=consider-using-with

f = open("fruits.txt", "r", encoding="utf8")
fruits = list(f)
print(fruits)
f.close()
