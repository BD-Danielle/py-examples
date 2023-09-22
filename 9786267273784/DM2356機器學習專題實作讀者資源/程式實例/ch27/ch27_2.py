# ch27_2.py
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# 電影數據
movies = np.array([
    [8, 7],     # 動作片1
    [9, 8],     # 動作片2
    [10, 9],    # 動作片3
    [7, 6],     # 動作片4
    [1, 2],     # 喜劇片1
    [2, 1],     # 喜劇片2
    [3, 4],     # 喜劇片3
])

# 電影類型, 動作片為0, 喜劇片為1
labels = np.array([0, 0, 0, 0, 1, 1, 1])

# 創建KNN分類器, 選擇3個最近鄰
knn = KNeighborsClassifier(n_neighbors=3)

# 擬合模型
knn.fit(movies, labels)

# Kwei的電影偏好
Kwei_movies = np.array([6, 7]).reshape(1, -1)

# 預測Kwei的電影類型
prediction = knn.predict(Kwei_movies)

# 印出預測結果
if prediction == 0:
    print("推薦動作片給Kwei")
else:
    print("推薦喜劇片給Kwei")


