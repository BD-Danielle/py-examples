# ch8_3.py
import matplotlib.pyplot as plt                                  
import numpy as np

x = np.array([1, 2, 3])         # 拜訪次數, 單位是100
y = np.array([5, 10, 20])       # 銷售考卷數, 單位是100

a, b = np.polyfit(x, y, 1)      # 迴歸直線
print(f'斜率 a = {a:.2f}')
print(f'截距 a = {b:.2f}')

y2 = a*x + b
plt.scatter(x, y)               # 繪製散佈圖
plt.plot(x, y2)                 # 繪製迴歸直線
plt.show()                      

