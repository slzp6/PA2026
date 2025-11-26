"""c5_4.py"""

# pylint: disable=unnecessary-lambda-assignment

import random

L = [random.randint(0, 10) for i in range(10)]
print("unsorted:", L)

qsort = lambda L: [] if L == [] else qsort([x for x in L[1:] if x < L[0]]) + L[
    0:1] + qsort([x for x in L[1:] if x >= L[0]])

print("sorted:  ", qsort(L))
