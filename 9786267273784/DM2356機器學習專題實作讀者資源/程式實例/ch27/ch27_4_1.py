# ch27_4_1.py
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# 生成數據集
X, y = make_blobs(n_samples=200, centers=2, random_state=8)

plt.scatter(X[:,0], X[:,1], c=y, edgecolor='b')    # 顯示散點圖

# 顯示圖形
plt.show()
