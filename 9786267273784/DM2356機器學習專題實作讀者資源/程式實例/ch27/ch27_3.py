# ch27_3.py
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

# 電影名稱
movie_names = np.array([
    "Mission Impossible",
    "搶救雷恩大兵",
    "玩命關頭",
    "雷神索爾",
    "真善美",
    "愛情停損點",
    "雙手的溫柔"
])

# 創建KNN分類器, 選擇3個最近鄰居
knn = KNeighborsClassifier(n_neighbors=3)

# 擬合模型
knn.fit(movies, labels)

# Kwei的電影喜好
Kwei_movies = np.array([8, 7]).reshape(1, -1)

# 找出與 Kwei 電影喜好 最接近的3部電影
distances, indices = knn.kneighbors(Kwei_movies)
print(f'最接近喜好的距離 : {distances}')
print(f'最接近喜好的索引 : {indices}')
print('='*70)

# indices 是二維陣列, 轉成串列 index
index = indices.flatten()

# 輸出與Kwei喜好最接近的3部電影
print("輸出 Kwei 喜好最接近的3部電影 : ")
for i in range(3):
    print(f"{movie_names[index[i]]} {movies[index[i]]}")


