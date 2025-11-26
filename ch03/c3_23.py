"""c3_23.py"""

method_l = [i for i in dir([]) if not i.startswith('_')]
method_t = [i for i in dir(()) if not i.startswith('_')]
print(method_l, len(method_l))
print(method_t, len(method_t))
