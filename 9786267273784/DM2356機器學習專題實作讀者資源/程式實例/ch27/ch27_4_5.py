# ch27_4_5.py
from sklearn.datasets import make_blobs
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import numpy as np

# 生成數據集
X, y = make_blobs(n_samples=500, centers=5, random_state=8)

k = 3
knn = KNeighborsClassifier(n_neighbors = k)
knn.fit(X, y)

# 設定繪圖區域
x_min, x_max = X[:,0].min() - 1, X[:,0].max() + 1
y_min, y_max = X[:,1].min() - 1, X[:,1].max() + 1

# 產生所有平面的座標點
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                     np.arange(y_min, y_max, 0.01))

# 將 xx, yy 先扁平化再組成二維陣列, 然後預估分類
Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)                 # 將 Z 與 xx 相同外形
plt.contourf(xx, yy, Z, alpha=0.3)      # 繪製填充等高線圖

# 顯示散點圖
plt.scatter(X[:,0], X[:,1], c=y, edgecolor='b')    

y_pred = knn.predict(X)                 # 用模型進行預測
accuracy = accuracy_score(y, y_pred)
print(f'準確率 : {accuracy:.3f}')  

# 顯示圖形
plt.show()


