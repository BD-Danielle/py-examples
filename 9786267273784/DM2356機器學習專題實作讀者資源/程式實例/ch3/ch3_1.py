# ch3_1.py
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False  # 負數符號

x = [x for x in range(0, 11)]                   
y = [(3 * y - 18) for y in x]
plt.plot(x, y, '-*')   
plt.xlabel("小孩人數")
plt.ylabel("蘋果數量")
plt.grid()                                  # 加格線
plt.show()


