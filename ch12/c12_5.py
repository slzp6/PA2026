"""c12_5.py"""


def read_file(filename):
    """read a file"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            contents = f.read()
            print(contents)
    except IOError:
        print("error: can not read file: " + filename)


read_file("fruits.txt")
read_file("fruits_na.txt")  # not available
