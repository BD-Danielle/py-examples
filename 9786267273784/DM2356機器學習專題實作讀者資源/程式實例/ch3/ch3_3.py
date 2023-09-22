# ch3_3.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False  # 負數符號

x = np.linspace(0, 1000, 100)
y = 0.03 * x - 18
plt.axis([0, 1000, -20, 15])            # 標記刻度範圍
plt.plot(x, y)   
plt.xlabel("來客數")
plt.ylabel("利潤")
plt.grid()                              # 加格線
plt.show()


