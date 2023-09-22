# ch28_7.py
from sklearn.datasets import make_circles
import matplotlib.pyplot as plt

# 生成數據
X, y = make_circles(n_samples=200, noise=0.05, random_state=10)

# 繪製數據點，分類A使用圈圈'o', 分類B使用星型'*', 加入 label 參數
for i, marker in zip([0, 1], ['o', '*']):
    plt.scatter(X[y == i, 0], X[y == i, 1], marker=marker, label=i) 

plt.show()



