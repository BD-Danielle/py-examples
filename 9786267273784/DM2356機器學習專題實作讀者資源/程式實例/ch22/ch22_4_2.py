# ch22_4_2.py
from sklearn.datasets import make_circles
import matplotlib.pyplot as plt

# 生成數據
X, y = make_circles(n_samples=100, noise=0.05, random_state=10)

# 繪製數據
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.show()


