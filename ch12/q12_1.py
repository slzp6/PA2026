"""q12_1.py"""

# pylint: disable=consider-using-with

F = "test_1.txt"

f = open(F, "w", encoding="utf8")
f.write("abc")
f.close()

f = open(F, "a", encoding="utf8")
f.write("def")
f.close()

f = open(F, "r", encoding="utf8")
T = f.read()
f.close()

print(T)
