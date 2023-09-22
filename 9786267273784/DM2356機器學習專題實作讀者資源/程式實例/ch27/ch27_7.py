# ch27_7.py
from sklearn.neighbors import KNeighborsRegressor
import numpy as np

# 訓練數據, 例如房子的面積（單位 : 坪）和房齡（年）
X_train = np.array([[50, 15], [80, 10], [120, 5], [150, 3],
                    [200, 2], [250, 1], [300, 0.5]])

# 目標數值, 例如房價（單位：萬元）
y_train = np.array([180, 280, 360, 420, 580, 720, 850])

# 創建KNN回歸模型, 選擇3個最近鄰居
knn_reg = KNeighborsRegressor(n_neighbors=3)

# 擬合模型
knn_reg.fit(X_train, y_train)

# 預測新的房子的價格
X_new = np.array([[180, 7]])  # 面積為100坪, 房齡為7年
y_pred = knn_reg.predict(X_new)

# 輸出預測結果
print(f"{X_new[0,0]}坪, {X_new[0,1]}年的房價預估 : {y_pred[0]:.2f}萬元")


