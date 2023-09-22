# ch22_5.py
from sklearn.datasets import make_classification
import matplotlib.pyplot as plt

# 生成一個 100 個樣本、2 個特徵(因此可以在二維平面上繪製)的數據集
# 有 2 個信息特徵、無冗餘特徵、無重複特徵，並且有 2 個類別
X, y = make_classification(n_samples=100, n_features=2,
       n_informative=2, n_redundant=0, n_repeated=0, n_classes=2,
       random_state=1)

# 繪製生成的數據集
plt.scatter(X[:, 0], X[:, 1], marker='o', c=y, s=25, edgecolor='k')
plt.show()


