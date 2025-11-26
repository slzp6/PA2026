"""c12_8.py"""

FILE_PATH = r"hello.txt"
with open(FILE_PATH, "w", encoding="utf8") as f:
    f.write("Hello, World!")
