# ch27_4_4.py
from sklearn.datasets import make_blobs
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import numpy as np

# 生成數據集
X, y = make_blobs(n_samples=200, centers=2, random_state=30)

# 設定繪圖區域
x_min, x_max = X[:,0].min() - 1, X[:,0].max() + 1
y_min, y_max = X[:,1].min() - 1, X[:,1].max() + 1

# 產生所有平面的座標點
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                     np.arange(y_min, y_max, 0.01))

k_values = [5, 7, 29, 49]                   # 設定 k 值串列

# 建立 4 個子圖
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

for k, ax in zip(k_values, axs.ravel()):    # 迴圈繪製分類圖形
    knn = KNeighborsClassifier(n_neighbors = k)
    knn.fit(X, y)
    
    # 將 xx, yy 先扁平化再組成二維陣列, 然後預估分類
    Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)                 # 將 Z 與 xx 相同外形
    ax.contourf(xx, yy, Z, alpha=0.3)       # 繪製填充等高線圖

    # 顯示散點圖
    ax.scatter(X[:,0], X[:,1], c=y, edgecolor='b')
    ax.set_title('KNN, Random_State=30, k={}'.format(k))

# 顯示圖形
plt.subplots_adjust(wspace=0.2, hspace=0.4)  # 調整子圖之間的間距
plt.show()



