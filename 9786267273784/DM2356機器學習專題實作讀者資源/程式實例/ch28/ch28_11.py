# ch28_11.py
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn import svm

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False  # 負數符號
# 建立 50 個點, 其中25個分類為0, 25個分類為1
X, y = make_blobs(n_samples=50, centers=2, random_state=12)

# 建立一個線性SVM模型
svc = svm.SVC(kernel='linear')
svc.fit(X, y)

# 繪製數據點, 分類0使用圈圈'o', 分類1使用星型'*'
for i, marker in zip([0, 1], ['o', '*']):
    plt.scatter(X[y == i, 0], X[y == i, 1], marker=marker, label=str(i))

ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()

# 建立格點來評估模型
xx = np.linspace(xlim[0], xlim[1], 30)
yy = np.linspace(ylim[0], ylim[1], 30)
XX, YY = np.meshgrid(xx, yy)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = svc.decision_function(xy).reshape(XX.shape)

# 繪製決策邊界和超平面
ax.contour(XX, YY, Z, colors='b', levels=[-1, 0, 1], alpha=0.5,
           linestyles=['--', '-', '--'])

# 繪製支援向量
ax.scatter(svc.support_vectors_[:, 0], svc.support_vectors_[:, 1],
           s=100, facecolors='none', edgecolors='k')

plt.title("支援向量機 - kernel='linear'")
plt.legend()
plt.show()


