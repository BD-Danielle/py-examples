# ch15_4.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.01, 0.99, 100)        # 建立含1000個元素的陣列
y = [np.log(x/(1-x)) for x in x]        # logit函數
plt.axis([0, 1, -5, 5])
plt.plot(x, y, label="Logit function")
plt.plot(0.5, np.log(0.5/(1-0.5)),'-o')

plt.legend(loc="best")                  # 建立圖例
plt.grid()
plt.show()




