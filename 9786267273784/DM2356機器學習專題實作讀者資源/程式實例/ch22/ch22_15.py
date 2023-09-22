# ch22_15.py
from sklearn.linear_model import LinearRegression
import numpy as np

height = np.array([1.6, 1.63, 1.71, 1.73, 1.83]).reshape(-1,1)
weight = np.array([55, 58, 62, 65, 71])

model = LinearRegression()          # 建立線性迴歸的模型
model.fit(X=height, y=weight)       # 數據擬合模型

# 手工計算 RSS
RSS = np.sum((weight - np.ravel(model.predict(height))) ** 2)
print(f"總平方和 RSS : {RSS:.2f}")

# 手工計算 TSS
mean_weight = np.mean(weight)
TSS = np.sum((np.ravel(weight) - mean_weight) ** 2)
print(f"總平方和 TSS : {TSS:.2f}")

# 手工計算R平方係數
R_square = 1 - (RSS / TSS)
print(f"手工計算 - R平方係數 : {R_square:.2f}")

# 使用 score() 函數計算 R平方係數
R_score = model.score(height, weight)
print(f"函數計算 - R平方係數 : {R_score:.2f}")
      








