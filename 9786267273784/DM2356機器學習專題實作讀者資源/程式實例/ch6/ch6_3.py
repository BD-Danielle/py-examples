# ch6_2.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False  # 負數符號

plt.plot([0, 20], [0, 0])           # 繪公式 1, 水平線
#plt.plot([0, 0], [0, 20])           # 繪公式 2, 垂直線
                                


plt.plot(5, 5, '-o')                # 繪交叉點
plt.text(4.5, 5.5, '(5, 5)')        # 輸出(5, 5)
plt.xlabel("商用軟體")
plt.ylabel("App 軟體")
plt.grid()                          # 加格線
plt.show()






