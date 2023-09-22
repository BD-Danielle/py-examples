# ch27_8_1.py
import matplotlib.pyplot as plt
from sklearn.datasets import make_regression

# 生成線性數據集
X, y = make_regression(n_features=1, noise=20, random_state=10)

plt.scatter(X, y, c='y', edgecolor='b')         # 顯示散點圖
plt.show()


