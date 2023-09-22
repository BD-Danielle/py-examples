# ch27_4.py
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# distance是射門距離, angle是射門角度, goal是否進球
distance = [10, 20, 10, 30, 20, 30, 15, 25, 20, 15]
angle = [30, 45, 60, 30, 60, 75, 45, 60, 75, 90]
goal = [1, 1, 0, 1, 0, 0, 1, 0, 0, 1]   # 0 是沒進, 1 是進球

# 將數據整理成適合的格式
X = np.column_stack((distance, angle))
y = np.array(goal)

# 建立和訓練模型
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X, y)

# 獲取使用者輸入的新球員數據
new_distance = float(input("請輸入射門距離 (單位是公尺) : "))
new_angle = float(input("請輸入射門角度 : "))
new_player = np.array([[new_distance, new_angle]])

# 預測球員是否能進球
prediction = neigh.predict(new_player)
prediction_proba = neigh.predict_proba(new_player)

# 輸出結果
print(f"是否進球(0是沒進, 1是進球) : {prediction}")
print(f"不進球機率                 : {prediction_proba[0][0]:.3f}")
print(f"進球機率                   : {prediction_proba[0][1]:.3f}")









