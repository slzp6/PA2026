"""q9_2.py"""


def make_pretty(func):
    """make pretty"""

    def wrapper():
        print("decorated")
        func()

    return wrapper


@make_pretty
def ordinary():
    """ordinary function"""
    print("ordinary")


ordinary()
