# ch22_7.py
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

height = np.array([1.6, 1.63, 1.71, 1.73, 1.83]).reshape(-1,1)
weight = np.array([55, 58, 62, 65, 71])

plt.plot(height, weight, 'ko')
plt.axis([1.5, 1.85, 50, 90])
plt.xlabel("身高")
plt.ylabel("體重")
plt.title("身高 vs 體重")

model = LinearRegression()          # 建立線性迴歸的模型
model.fit(X=height, y=weight)       # 數據擬合模型
y_pred = model.predict(height)      # 預測 體重 數據
plt.plot(height, y_pred, c='r')     # 繪製預測迴歸線

plt.grid()
plt.show()







