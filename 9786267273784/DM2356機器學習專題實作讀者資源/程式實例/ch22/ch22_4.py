# ch22_4.py
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# 生成 2 個數據集
X1, y1 = make_blobs(n_samples=500,n_features=2,centers=5,random_state=1)
X2, y2 = make_blobs(n_samples=300,n_features=2,centers=3,random_state=1)

# 建立子圖
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

# 繪製第 1 個數據集
axs[0].scatter(X1[:, 0], X1[:, 1], c=y1)
axs[0].set_title('First dataset')

# 繪製第 2 個數據集
axs[1].scatter(X2[:, 0], X2[:, 1], c=y2)
axs[1].set_title('Second dataset')

# 顯示圖形
plt.show()



