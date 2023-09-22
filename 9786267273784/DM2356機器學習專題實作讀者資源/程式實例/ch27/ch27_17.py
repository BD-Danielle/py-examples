# ch27_17.py
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 下載 iris 數據集
iris = load_iris()
X = iris.data[:, :2]  # 只取前兩個特徵,即sepal length和sepal width
y = iris.target

# 設定繪圖區域
x_min, x_max = X[:,0].min() - 1, X[:,0].max() + 1
y_min, y_max = X[:,1].min() - 1, X[:,1].max() + 1

# 產生所有平面的座標點
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                     np.arange(y_min, y_max, 0.01))

fig, axs = plt.subplots(2, 2, figsize=(10, 10))
k_values = [3, 5, 29, 49]
for k, ax in zip(k_values, axs.ravel()):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X, y)    
    # 將 xx, yy 先扁平化再組成二維陣列, 然後預估分類
    Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)                 # 將 Z 與 xx 相同外形
    ax.contourf(xx, yy, Z, alpha=0.3)       # 繪製填充等高線圖

    # 顯示散點圖
    scatter = ax.scatter(X[:,0], X[:,1], c=y, edgecolor='b')    
    
    # 增加圖例
    handles, labels = scatter.legend_elements()
    ax.legend(handles, iris.target_names, title="鳶尾花品種")
    ax.set_title(f'KNN for 鳶尾花Iris, k = {k}')
    ax.set_xlabel('花萼長度sepal length')
    ax.set_ylabel('花萼寬度sepal width')

plt.subplots_adjust(wspace=0.2, hspace=0.4)  # 調整子圖之間的間距
plt.show()
