"""c7_16.py"""


def vl_func(**x):
    """simple function"""
    print(type(x))
    print(x)
    for i in x.items():
        print(i)


vl_func(a=10, b=20, c="OUJ")
