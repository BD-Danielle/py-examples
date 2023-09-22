# ch28_6_2.py
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 建立10個點, 其中5個分類為A, 5個分類為B
X = np.array([[1, 2.5], [0.5, 2], [2, 2], [1.5, 1], [2.5, 1.3],
              [3, 3.5], [4.5, 3.5], [4, 4], [2.5, 4.5], [3.5, 3]])
y = np.array(['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B'])

# 建立一個線性SVM模型
svc = svm.SVC(kernel='linear')
svc.fit(X, y)

# 繪製數據點, 分類A使用圈圈'o', 分類B使用星型'*'
for i, marker in zip(['A', 'B'], ['o', '*']):
    plt.scatter(X[y == i, 0], X[y == i, 1], marker=marker, label=i)

ax = plt.gca()

# 建立格點來評估模型
xx = np.linspace(0, 5)
yy = np.linspace(0, 5)
XX, YY = np.meshgrid(xx, yy)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = svc.decision_function(xy).reshape(XX.shape)

# 繪製決策邊界和間隔
ax.contour(XX, YY, Z, colors='b', levels=[-1, 1], alpha=0.5,
           linestyles=['--','--'])

# 用圈圈繪製支援向量
ax.scatter(svc.support_vectors_[:, 0], svc.support_vectors_[:, 1],
           s=100, facecolors='none', edgecolors='k')
plt.title('支援向量機 - 繪製超平面和決策邊界')
plt.xlabel(r'$x_{1}$', fontsize=14)
plt.ylabel(r'$x_{2}$', fontsize=14)
plt.legend()
plt.show()


