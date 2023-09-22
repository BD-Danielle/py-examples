# ch28_3.py
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from joblib import dump

plt.rcParams["font.family"] = ["Microsoft JhengHei"]
# 建立10個點, 其中5個分類為A, 5個分類為B
X = np.array([[1, 2.5], [0.5, 2], [2, 2], [1.5, 1], [2.5, 1.3],
              [3, 3.5], [4.5, 3.5], [4, 4], [2.5, 4.5], [3.5, 3]])
y = np.array(['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B'])

# 繪製數據點，分類A使用圈圈'o', 分類B使用星型'*', 加入 label 參數
for i, marker in zip(['A', 'B'], ['o', '*']):
    plt.scatter(X[y == i, 0], X[y == i, 1], marker=marker, label=i) 

svc = svm.SVC(kernel = 'linear')                # 建立 linear的 svc
svc.fit(X, y)                                   # 訓練 svc

w = svc.coef_[0]                                # 權重 weights
slope = -w[0] / w[1]                            # 斜率 slope
b = svc.intercept_[0]                           # 偏置值(截距)
dump(svc, 'svc28_3.joblib')                     # 儲存模型

# 繪製超平面
xx = np.linspace(0, 5)                          # x1 預設50點
yy = slope * xx - (b / w[1])                    # 計算 x2 
plt.plot(xx, yy, linewidth=2, color='green')

# 繪製決策邊界 1, 左下方
sv = svc.support_vectors_[0]                    # 第 1 個決策向量
yy_1 = slope * xx + (sv[1] - slope * sv[0])     # 計算 y = ax + b
plt.plot(xx, yy_1, 'b--')

# 繪製決策邊界 2, 右上方
sv = svc.support_vectors_[-1]                   # 最後 1 個決策向量
yy_2 = slope * xx + (sv[1] - slope * sv[0])     # 計算 y = ax + b
plt.plot(xx, yy_2, 'b--')

# 用圈圈繪製支援向量
plt.scatter(svc.support_vectors_[:, 0], svc.support_vectors_[:, 1],
            s=100, facecolors='none', edgecolors='k')

plt.ylim(0, 5)
plt.xlim(0, 5)
plt.title('支援向量機 - 繪製超平面和決策邊界')
plt.xlabel(r'$x_{1}$', fontsize=14)
plt.ylabel(r'$x_{2}$', fontsize=14)
plt.legend()
plt.show()












