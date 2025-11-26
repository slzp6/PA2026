"""c3_15.py"""

import copy

mylist = ['a', 'b', ['c', 'd'], 'e']
cp_shallow = mylist.copy()
cp_shallow[0] = 'A'
cp_shallow[2][0] = 'C'
print('mylist :', mylist)
print('shallow:', cp_shallow)

print("---")
mylist = ['a', 'b', ['c', 'd'], 'e']
cp_deep = copy.deepcopy(mylist)
cp_deep[0] = 'A'
cp_deep[2][0] = 'C'
print('mylist: ', mylist)
print('deep:   ', cp_deep)
