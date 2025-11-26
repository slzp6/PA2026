"""c7_17.py"""


def func(pos_a, pos_b, /, pos_or_kwd, *, kwd_a, kwd_b):
    """function"""
    print(pos_a, pos_b, pos_or_kwd, kwd_a, kwd_b)


func(10, 20, pos_or_kwd=30, kwd_a=40, kwd_b=50)
func(100, 200, 300, kwd_a=400, kwd_b=500)
func(100, 200, 300, kwd_b=5000, kwd_a=4000)
