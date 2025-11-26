"""c7_9.py"""

# pylint: disable=global-statement

G = 1


def func():
    """function"""
    global G  #  (global-statement)
    G = 100
    print(G)


func()
print(G)
