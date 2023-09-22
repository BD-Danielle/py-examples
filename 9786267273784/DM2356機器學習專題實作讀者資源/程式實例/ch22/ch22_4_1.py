# ch22_4_1.py
from sklearn.datasets import make_moons
import matplotlib.pyplot as plt

# 生成數據
X, y = make_moons(n_samples=200, noise=0.05, random_state=0)

# 可視化數據
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.show()


