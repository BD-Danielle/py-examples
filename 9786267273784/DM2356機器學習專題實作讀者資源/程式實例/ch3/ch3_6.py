# ch3_6.py
import matplotlib.pyplot as plt
                                
x = [x for x in range(0, 11)]
y1 = [2 * y for y in x]             # Line 1
y2 = [3 * y for y in x]             # Line 2
y3 = [4 * y for y in x]             # Line 3
plt.xticks(x)
plt.plot(x, y1, label='L1')
plt.plot(x, y2, label='L2')
plt.plot(x, y3, label='L3')
plt.legend(loc='best')
plt.grid()                          # 加格線
plt.show()


