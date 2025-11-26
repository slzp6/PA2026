"""c5_3.py"""

# pylint: disable=comparison-of-constants
# pylint: disable=expression-not-assigned

COND = 10 > 20
IF_TRUE = "10 is greater than 20"
IF_FALSE = "20 is greater than 10"

# a  (if-else)
if COND:
    print(IF_TRUE)
else:
    print(IF_FALSE)

# b  (ternary operator)
print(IF_TRUE) if COND else print(IF_FALSE)

# c  (tuple)
T = (IF_FALSE, IF_TRUE)[COND]
print(T)

# d  (dictionary)
D = {True: IF_TRUE, False: IF_FALSE}[COND]
print(D)

# e  (lambda function)
E = (lambda: IF_FALSE, lambda: IF_TRUE)[COND]()
print(E)
