# ch22_13.py
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False  # 負數符號

height = np.array([1.6, 1.63, 1.71, 1.73, 1.83]).reshape(-1,1)
weight = np.array([55, 58, 62, 65, 71])

plt.plot(height, weight, 'ko')
plt.axis([0, 1.9, -150, 150])
plt.xlabel("身高")
plt.ylabel("體重")
plt.title("身高 vs 體重")

model = LinearRegression()          # 建立線性迴歸的模型
model.fit(X=height, y=weight)       # 數據擬合模型

x_line = np.array([0, 1.9]).reshape(-1,1)
y_pred = model.predict(x_line)      # 0 和 190的預測數據
plt.plot(x_line, y_pred, c='r')     # 繪製預測迴歸線

plt.grid()
plt.show()







