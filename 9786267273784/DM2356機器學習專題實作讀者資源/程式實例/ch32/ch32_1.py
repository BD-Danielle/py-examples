# ch32_1.py
import numpy as np
from sklearn.decomposition import PCA

# 假設我們有以下的3維數據集, 包含了5個樣本
X = np.array([
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 5],
    [4, 5, 6],
    [5, 6, 7]
])

# 現在我們希望用PCA將這個3維的數據降維到2維
pca = PCA(n_components=2)

# 對數據進行PCA轉換
X_new = pca.fit_transform(X)

# 印出降維後的數據
print(f'降維結果\n{X_new}')
print(f'特徵平均值 : {pca.mean_}')
print(f'輸入特徵數量 : {pca.n_features_}')
print(f'輸入樣本數量 : {pca.n_samples_}')
print(f'主成分數量   : {pca.n_components}')


