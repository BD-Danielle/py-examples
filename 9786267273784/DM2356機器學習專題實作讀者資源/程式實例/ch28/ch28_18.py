# ch28_18.py
from sklearn.svm import SVR
import numpy as np

# 定義特徵和目標變數
X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
y = np.array([0.5, 1.5, 2.5, 3.5])

# 創建並訓練線性核的SVR模型
model_linear = SVR(kernel='linear', C=1.0, epsilon=0.1)
model_linear.fit(X, y)

# 創建並訓練RBF核的SVR模型
model_rbf = SVR(kernel='rbf', C=1.0, epsilon=0.1)
model_rbf.fit(X, y)

# 使用線性核的模型進行預測
y_pred_linear = model_linear.predict(X)

# 使用RBF核的模型進行預測
y_pred_rbf = model_rbf.predict(X)

# 輸出預測結果
for i in range(len(y)):
    print(f'目標變數:{y[i]}, 線性核預測結果:{y_pred_linear[i]:.3f},', end=" ")
    print(f'RBF核預測結果:{y_pred_rbf[i]:.3f}')



