# ch27_1.py
from sklearn.neighbors import KNeighborsClassifier
X = [[0], [1], [2], [3]]
y = [0, 0, 1, 1]
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)

x = 1.1
print(f'x = {x} 分類是   : {knn.predict([[x]])}')
print(f'x = {x} 分類機率 : {knn.predict_proba([[x]])}')

x = 1.6
print(f'x = {x} 分類是   : {knn.predict([[x]])}')
print(f'x = {x} 分類機率 : {knn.predict_proba([[x]])}')

