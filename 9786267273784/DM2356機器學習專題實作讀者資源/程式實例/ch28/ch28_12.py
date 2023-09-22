# ch28_12.py
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn import svm

# 設定字型和負數符號
plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False

# 建立 50 個點, 其中25個分類為0, 25個分類為1
X, y = make_blobs(n_samples=50, centers=2, random_state=12)

# 繪製子圖, 每個 gamma 值一張圖
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(10,10))
ax = np.ravel(ax)

gammas = [0.1, 0.5, 1.0, 10.0]

for i, gamma in enumerate(gammas):
    # 建立一個 RBF SVM 模型
    svc = svm.SVC(kernel='rbf', gamma=gamma)
    svc.fit(X, y)

    # 繪製數據點, 分類0使用圈圈'o', 分類1使用星型'*'
    for j, marker in zip([0, 1], ['o', '*']):
        ax[i].scatter(X[y == j, 0], X[y == j, 1], marker=marker,
                      label=str(j))

    xlim = ax[i].get_xlim()
    ylim = ax[i].get_ylim()

    # 建立格點來評估模型
    xx = np.linspace(xlim[0], xlim[1], 30)
    yy = np.linspace(ylim[0], ylim[1], 30)
    XX, YY = np.meshgrid(xx, yy)
    xy = np.vstack([XX.ravel(), YY.ravel()]).T
    Z = svc.decision_function(xy).reshape(XX.shape)

    # 繪製決策邊界和超平面
    ax[i].contour(XX, YY, Z, colors='b', levels=[-1, 0, 1], alpha=0.5,
                  linestyles=['--', '-', '--'])

    # 繪製支援向量
    ax[i].scatter(svc.support_vectors_[:, 0], svc.support_vectors_[:, 1],
                  s=100, facecolors='none', edgecolors='k')
    
    ax[i].set_title(f"支援向量機 - kernel='rbf', gamma={gamma}")
    ax[i].legend()

# 調整子圖之間的間距
plt.subplots_adjust(wspace=0.2, hspace=0.4)
plt.show()


