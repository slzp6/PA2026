"""c10_4.py"""

import pprint

S = "The Open University of Japan"
M = [i for i in dir(S) if "__" not in i]
pprint.pprint(M, compact=True)
print(len(M))
