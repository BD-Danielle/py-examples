# ch27_6.py
from sklearn.neighbors import KNeighborsRegressor
import numpy as np

# 訓練數據, 例如房子的面積（單位 : 坪）
X_train = np.array([50, 80, 120, 150, 200, 250, 300]).reshape(-1, 1)

# 目標數值, 例如房價（單位 : 萬元）
y_train = np.array([180, 280, 360, 420, 580, 720, 850])

# 創建KNN回歸模型, 選擇3個最近鄰居
knn_reg = KNeighborsRegressor(n_neighbors=3)

# 擬合模型
knn_reg.fit(X_train, y_train)

# 預測新的房子的價格
X_new = np.array([110]).reshape(-1, 1)
y_pred = knn_reg.predict(X_new)

# 印出預測結果
print(f"{X_new[0,0]} 坪的房子預估價格為 : {y_pred[0]:.2f} 萬元")



