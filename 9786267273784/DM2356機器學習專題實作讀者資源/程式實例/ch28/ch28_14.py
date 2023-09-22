# ch28_14.py
from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = ["Microsoft JhengHei"]

# 下載 iris 數據集
iris = load_iris()

# 用後兩個特徵,花瓣長度(petal length)和花瓣寬度(petal width)
X = iris.data[:, 2:]  
y = iris.target

# 設定繪圖區域
x_min, x_max = X[:,0].min() - 0.2, X[:,0].max() + 1
y_min, y_max = X[:,1].min() - 0.2, X[:,1].max() + 1

# 產生所有平面的座標點
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                     np.arange(y_min, y_max, 0.01))

kernels = ['linear', 'rbf', 'rbf', 'poly']
gamma_values = ['scale', 0.5, 100, 'scale']   # for rbf and poly kernels
titles = ['Linear kernel', 'RBF kernel, gamma=0.5',
          'RBF kernel, gamma=100', 'Poly kernel']

fig, sub = plt.subplots(2, 2, figsize=(10, 10))
plt.subplots_adjust(wspace=0.4, hspace=0.4)  # 調整子圖空間
sub = sub.flatten()

for kernel, gamma, title, ax in zip(kernels, gamma_values, titles, sub):
    model = SVC(kernel=kernel, gamma=gamma)
    model.fit(X, y)

    # 將 xx, yy 先扁平化再組成二維陣列, 然後預估分類
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)                 # 將 Z 與 xx 相同外形
    ax.contourf(xx, yy, Z, alpha=0.3)       # 繪製填充等高線圖

    # 顯示散點圖
    scatter = ax.scatter(X[:,0], X[:,1], c=y, edgecolor='b')    

    # 增加圖例
    handles, labels = scatter.legend_elements()
    ax.legend(handles, iris.target_names, title="鳶尾花品種")

    ax.set_title(title + f'(accuracy:{accuracy_score(y,model.predict(X)):.2f})')
    ax.set_xlabel('花瓣長度petal length')
    ax.set_ylabel('花瓣寬度petal width')

plt.show()
