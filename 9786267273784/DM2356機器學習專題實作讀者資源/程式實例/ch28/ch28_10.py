# ch28_10.py
from sklearn.datasets import make_circles
import matplotlib.pyplot as plt
from sklearn import svm
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
plt.rcParams["axes.unicode_minus"] = False  # 負數符號
# 生成數據
X, y = make_circles(n_samples=300, noise=0.05, random_state=10)
z = X[:,0]**2 + X[:,1]**2

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# 繪製數據點, 分類A使用圈圈'o', 分類B使用星型'*', 加入 label 參數
for i, marker in zip([0, 1], ['o', '*']):
    ax.scatter(X[y == i, 0], X[y == i, 1], z[y == i], marker=marker,
               label=str(i)) 

features = np.concatenate((X, z.reshape(-1,1)), axis=1)
svc = svm.SVC(kernel = 'linear')
svc.fit(features, y)

x3 = lambda x, y : (-svc.intercept_[0] - svc.coef_[0][0] *
                    x - svc.coef_[0][1] * y) / svc.coef_[0][2]

grid = np.linspace(-1.5,1.5)                # 分割繪圖區間
xx, yy = np.meshgrid(grid, grid)            # 建立 mesh 網格
ax.plot_surface(xx, yy, x3(xx, yy), alpha=0.3)
plt.title('支援向量機 - 繪製 3D 超平面')
plt.xlabel(r'$x_{1}$', fontsize=14)
plt.ylabel(r'$x_{2}$', fontsize=14)
plt.show()


