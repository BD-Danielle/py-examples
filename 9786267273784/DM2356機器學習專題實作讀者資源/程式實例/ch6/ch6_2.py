# ch6_2.py
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

plt.plot([0, 20], [0, 0])           # 繪公式 1, 水平線
plt.plot([0, 0], [0, 20])           # 繪公式 2, 垂直線
                                
line3_x = np.linspace(0, 20, 20)
line3_y = [(8 - 0.6 * x) for x in line3_x]

line4_x = np.linspace(0, 20, 20)
line4_y = [(17.5 - 2.5 * x) for x in line4_x]

lineobj_x = np.linspace(0, 20, 20)
lineobj_y = [10 - x for x in lineobj_x]

plt.axis([0, 20, 0, 20])

plt.plot(line3_x, line3_y)          # 繪公式 3
plt.plot(line4_x, line4_y)          # 繪公式 4
plt.plot(lineobj_x, lineobj_y)      # 繪目標公式 5

plt.plot(5, 5, '-o')                # 繪交叉點
plt.text(4.5, 5.5, '(5, 5)')        # 輸出(5, 5)
plt.xlabel("商用軟體")
plt.ylabel("App 軟體")
plt.grid()                          # 加格線
plt.show()






