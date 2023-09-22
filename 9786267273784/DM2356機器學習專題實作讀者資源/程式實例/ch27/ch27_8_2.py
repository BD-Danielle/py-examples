# ch27_8_2.py
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression
from sklearn.neighbors import KNeighborsRegressor
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False  # 負數符號

# 生成線性數據集
X, y = make_regression(n_features=1, noise=20, random_state=10)

k_values = [2, 3, 4, 5]

fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# 建立區間 X 軸內含 300 個點
xx = np.linspace(X.min(), X.max(), 300).reshape(-1,1)

for k, ax in zip(k_values, axs.ravel()):
    knn = KNeighborsRegressor(n_neighbors=k)    # 建立KNN物件
    knn.fit(X, y)                               # 擬合 KNN 模型

    r2 = knn.score(X, y)                        # R平方係數
    print(f'k={k}, R平方係數 : {r2:.3f}')   

    yy = knn.predict(xx)                        # 預估 Y 軸值
    ax.plot(xx, yy)                             # 繪製迴歸線
    ax.scatter(X, y, c='y', edgecolor='b')      # 顯示散點圖
    ax.set_title(f'KNN-Regression, k={k}, R平方係數={r2:.3f}')

plt.subplots_adjust(wspace=0.2, hspace=0.4)  # 調整子圖之間的間距
plt.show()



