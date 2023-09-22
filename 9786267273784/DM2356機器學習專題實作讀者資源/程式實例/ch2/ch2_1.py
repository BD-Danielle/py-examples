# ch2_1.py
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
unitprice = 90                      # 一斤的價格
x = [x for x in range(1, 11)]       # x代表斤
y = [y * unitprice for y in x]      # 不同重量的價格
plt.plot(x, y, '-*')
plt.title("玉荷包 重量 vs 價格表")
plt.xlabel("重量")
plt.ylabel("價格")
plt.show()


