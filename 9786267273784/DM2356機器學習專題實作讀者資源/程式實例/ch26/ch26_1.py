# ch26_1.py
from sklearn.ensemble import RandomForestRegressor
import numpy as np

# 建立一個小型的數據集
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])
y = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

# 建立隨機森林模型
rf = RandomForestRegressor(n_estimators=100, random_state=42)

# 訓練模型
rf.fit(X, y)

# 進行預測
X_new = np.array([[5.5], [6.5], [7.5]])
predictions = rf.predict(X_new)

print("預測結果:", predictions)

