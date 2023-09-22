# ch27_5.py
from sklearn.neighbors import KNeighborsRegressor

X = [[0], [1], [2], [3]]
y = [0, 0, 1, 2]

knn = KNeighborsRegressor(n_neighbors=2)
knn.fit(X, y) 

x = 1.5
print(f'x = {x} --> {knn.predict([[x]])}')
x = 2.5
print(f'x = {x} --> {knn.predict([[x]])}')







