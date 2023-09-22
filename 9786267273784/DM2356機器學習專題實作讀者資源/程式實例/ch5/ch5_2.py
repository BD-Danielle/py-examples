# ch5_2.py
import numpy as np

# 定義兩個向量
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# 計算向量之間的距離
distance = np.sqrt(np.sum((a - b) ** 2))

print(f"a and b 的距離 : {distance:.3f}")

