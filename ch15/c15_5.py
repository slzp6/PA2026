"""c15_5.py"""

from sklearn import datasets
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import neighbors

iris = datasets.load_iris()
x = iris['data']
y = iris['target']

x_train, x_test, y_train, y_test = \
train_test_split(iris['data'], iris['target'], random_state=100)
print("train:", len(x_train))
print("test:", len(x_test))

classifier = neighbors.KNeighborsClassifier(n_neighbors=5)
classifier.fit(x_train, y_train)
predictions = classifier.predict(x_test)
print(accuracy_score(y_test, predictions))
