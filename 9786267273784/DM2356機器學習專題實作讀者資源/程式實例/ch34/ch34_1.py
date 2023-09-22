# ch34_1.py
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.cluster import DBSCAN

# 生成二維數據
X, y = make_moons(n_samples=200, noise=0.05, random_state=0)

# 建立 DBSCAN 物件, 然後分群
db = DBSCAN(eps=0.3, min_samples=5)
db.fit(X)

# 獲取分群結果, 然後輸出分群的標籤
labels = db.labels_
print(f'輸出群集標籤\n{labels}')

# 繪製原始數據
plt.subplot(121)
plt.scatter(X[:,0], X[:,1], s=3)
plt.title('Original Data')
plt.gca().set_aspect('equal')       # 1:1 的比例

# 繪製分群結果
plt.subplot(122)
plt.scatter(X[:,0], X[:,1], c=labels, s=3)
plt.title('DBSCAN Clustering')
plt.gca().set_aspect('equal')       # 1:1 的比例

plt.subplots_adjust(wspace=0.4, hspace=0.4)
plt.show()


