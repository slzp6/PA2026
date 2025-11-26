"""c15_2.py"""

from sklearn.datasets import load_iris

iris = load_iris()
print(iris.keys())
print(type(iris['data']))
print(type(iris['target']))
print(iris['data'].shape)
print(iris['target'].shape)
