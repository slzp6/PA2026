"""c7_8.py"""

#pylint: disable=redefined-outer-name

i = 1


def func():
    """function"""

    i = 100
    print(i)


func()
print(i)
