# ch31_5.py
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import numpy as np

# 使用 make_blobs 產生數據
X, y = make_blobs(n_samples=300, centers=1, random_state=42)

# 使用 KMeans 進行分群
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

print("列印群集標籤")
print(kmeans.labels_)                       # 列印群集類別標籤
print("-"*70)
print("列印群集中心座標")
print(kmeans.cluster_centers_.round(2))     # 列印群集中心

# 設定繪圖區域
x_min, x_max = X[:,0].min() - 0.2, X[:,0].max() + 0.2
y_min, y_max = X[:,1].min() - 0.2, X[:,1].max() + 0.2

# 產生所有平面的座標點
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                     np.arange(y_min, y_max, 0.01))

# 將 xx, yy 先扁平化再組成二維陣列, 然後預估分類
Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)                     # 將 Z 與 xx 相同外形
plt.contourf(xx, yy, Z, alpha=0.3)          # 繪製填充等高線圖

# 繪製數據點
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap='viridis')

# 繪製群集中心
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
            s=200, c='red', marker='*')
plt.show()
