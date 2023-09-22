# ch22_8.py
from sklearn.linear_model import LinearRegression
import numpy as np

height = np.array([1.6, 1.63, 1.71, 1.73, 1.83]).reshape(-1,1)
weight = np.array([55, 58, 62, 65, 71])

model = LinearRegression()          # 建立線性迴歸的模型
model.fit(X=height, y=weight)       # 數據擬合模型

h = eval(input("請輸入身高(公分) : "))
h /= 100
weight_pred = model.predict([[h]])  # 預測 體重 數據
print(f"預估體重是 : {weight_pred[0]:.2f} 公斤")





