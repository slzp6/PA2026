"""c3_5.py"""

method_l = [i for i in dir([]) if not i.startswith('_')]
print(method_l, len(method_l))
