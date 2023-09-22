# ch28_19.py
import numpy as np
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler

# 創建模擬數據集
# 特徵 : 廣告支出(千元)和廣告時間(24小時制)
features = np.array([
    [500, 8],
    [700, 12],
    [300, 14],
    [400, 16],
    [600, 18],
    [800, 20],
    [900, 22],
    [200, 6],
    [100, 10],
    [450, 19]
])

# 目標變數 : 銷售(千元)
target = np.array([100, 150, 80, 120, 140, 180, 170, 60, 50, 130])

# 特徵標準化
scaler = StandardScaler()
features = scaler.fit_transform(features)

# 創建SVR模型
model = SVR(kernel='linear', C=1.0, epsilon=0.1)

# 使用特徵和目標值來訓練模型
model.fit(features, target)

# 使用訓練好的模型來預測新的數據點
new_data = np.array([[550, 15], [650, 21]])     # 新的廣告支出和廣時間
new_data = scaler.transform(new_data)           # 相同的標準化數據
y_pred = model.predict(new_data)

# 輸出預測結果
print(f'[550(費用:千元),15(小時)] : 預估銷售 {y_pred[0]:.2f}(千元)')
print(f'[650(費用:千元),21(小時)] : 預估銷售 {y_pred[1]:.2f}(千元)')

